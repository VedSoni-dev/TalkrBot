#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import ExecutionFeedback
import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path

class MemoryNode(Node):
    def __init__(self):
        super().__init__('memory_node')
        
        # Subscribe to execution feedback
        self.subscription = self.create_subscription(
            ExecutionFeedback,
            '/execution_feedback',
            self.feedback_callback,
            10
        )
        
        # Initialize database
        self.db_path = self.get_db_path()
        self.init_database()
        
        self.get_logger().info(f'MemoryNode initialized and subscribed to /execution_feedback')
        self.get_logger().info(f'Database: {self.db_path}')

    def get_db_path(self):
        """Get the database path, creating the directory if needed"""
        db_dir = Path.home() / '.talkrbot' / 'memory'
        db_dir.mkdir(parents=True, exist_ok=True)
        return db_dir / 'robot_memory.db'

    def init_database(self):
        """Initialize the SQLite database with required tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create execution feedback table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS execution_feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        step TEXT NOT NULL,
                        status TEXT NOT NULL,
                        notes TEXT,
                        timestamp TEXT NOT NULL,
                        created_at TEXT DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create user preferences table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_preferences (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        preference_type TEXT NOT NULL,
                        preference_value TEXT NOT NULL,
                        confidence REAL DEFAULT 1.0,
                        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create task patterns table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS task_patterns (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task_type TEXT NOT NULL,
                        success_rate REAL DEFAULT 0.0,
                        total_attempts INTEGER DEFAULT 0,
                        successful_attempts INTEGER DEFAULT 0,
                        common_failures TEXT,
                        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                conn.commit()
                self.get_logger().info('Database initialized successfully')
                
        except Exception as e:
            self.get_logger().error(f'Failed to initialize database: {e}')

    def feedback_callback(self, msg):
        """Process incoming execution feedback"""
        try:
            # Store the feedback
            self.store_feedback(msg)
            
            # Extract insights
            self.extract_insights(msg)
            
            # Log the memory update
            status_emoji = "✅" if msg.status == "success" else "❌"
            self.get_logger().info(f'{status_emoji} [MEMORY] Stored: {msg.step} → {msg.status}')
            
        except Exception as e:
            self.get_logger().error(f'Error processing feedback: {e}')

    def store_feedback(self, msg):
        """Store execution feedback in the database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO execution_feedback (step, status, notes, timestamp)
                    VALUES (?, ?, ?, ?)
                ''', (msg.step, msg.status, msg.notes, self.timestamp_to_str(msg.timestamp)))
                
                conn.commit()
                
        except Exception as e:
            self.get_logger().error(f'Failed to store feedback: {e}')

    def extract_insights(self, msg):
        """Extract insights from feedback and update patterns"""
        try:
            # Update task patterns
            self.update_task_patterns(msg)
            
            # Extract user preferences
            self.extract_user_preferences(msg)
            
        except Exception as e:
            self.get_logger().error(f'Error extracting insights: {e}')

    def update_task_patterns(self, msg):
        """Update task success/failure patterns"""
        try:
            # Extract task type from step (e.g., "go_to" from "go_to('closet')")
            task_type = msg.step.split('(')[0] if '(' in msg.step else msg.step
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if pattern exists
                cursor.execute('SELECT * FROM task_patterns WHERE task_type = ?', (task_type,))
                existing = cursor.fetchone()
                
                if existing:
                    # Update existing pattern
                    total_attempts = existing[5] + 1
                    successful_attempts = existing[6] + (1 if msg.status == "success" else 0)
                    success_rate = successful_attempts / total_attempts
                    
                    # Update common failures
                    common_failures = existing[7] or "{}"
                    failures_dict = json.loads(common_failures)
                    
                    if msg.status == "failure":
                        failure_type = msg.notes.split(':')[0] if ':' in msg.notes else "unknown"
                        failures_dict[failure_type] = failures_dict.get(failure_type, 0) + 1
                    
                    cursor.execute('''
                        UPDATE task_patterns 
                        SET success_rate = ?, total_attempts = ?, successful_attempts = ?, 
                            common_failures = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE task_type = ?
                    ''', (success_rate, total_attempts, successful_attempts, 
                          json.dumps(failures_dict), task_type))
                else:
                    # Create new pattern
                    success_rate = 1.0 if msg.status == "success" else 0.0
                    successful_attempts = 1 if msg.status == "success" else 0
                    common_failures = json.dumps({msg.notes.split(':')[0]: 1}) if msg.status == "failure" else "{}"
                    
                    cursor.execute('''
                        INSERT INTO task_patterns (task_type, success_rate, total_attempts, 
                                                 successful_attempts, common_failures)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (task_type, success_rate, 1, successful_attempts, common_failures))
                
                conn.commit()
                
        except Exception as e:
            self.get_logger().error(f'Error updating task patterns: {e}')

    def extract_user_preferences(self, msg):
        """Extract user preferences from feedback"""
        try:
            # Look for preference indicators in notes
            notes_lower = msg.notes.lower()
            
            preferences = []
            
            # Location preferences
            if "closet" in notes_lower and msg.status == "success":
                preferences.append(("location_preference", "closet", 0.8))
            if "kitchen" in notes_lower and msg.status == "success":
                preferences.append(("location_preference", "kitchen", 0.8))
            if "bedroom" in notes_lower and msg.status == "success":
                preferences.append(("location_preference", "bedroom", 0.8))
            
            # Object preferences
            if "blanket" in notes_lower and msg.status == "success":
                preferences.append(("object_preference", "blanket", 0.9))
            if "water" in notes_lower and msg.status == "success":
                preferences.append(("object_preference", "water", 0.9))
            if "pillow" in notes_lower and msg.status == "success":
                preferences.append(("object_preference", "pillow", 0.9))
            
            # Store preferences
            for pref_type, pref_value, confidence in preferences:
                self.store_user_preference(pref_type, pref_value, confidence)
                
        except Exception as e:
            self.get_logger().error(f'Error extracting user preferences: {e}')

    def store_user_preference(self, pref_type, pref_value, confidence):
        """Store user preference in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if preference already exists
                cursor.execute('''
                    SELECT * FROM user_preferences 
                    WHERE preference_type = ? AND preference_value = ?
                ''', (pref_type, pref_value))
                
                existing = cursor.fetchone()
                
                if existing:
                    # Update existing preference (increase confidence)
                    new_confidence = min(1.0, existing[3] + confidence * 0.1)
                    cursor.execute('''
                        UPDATE user_preferences 
                        SET confidence = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE preference_type = ? AND preference_value = ?
                    ''', (new_confidence, pref_type, pref_value))
                else:
                    # Create new preference
                    cursor.execute('''
                        INSERT INTO user_preferences (preference_type, preference_value, confidence)
                        VALUES (?, ?, ?)
                    ''', (pref_type, pref_value, confidence))
                
                conn.commit()
                
        except Exception as e:
            self.get_logger().error(f'Error storing user preference: {e}')

    def get_memory_context(self, limit=10):
        """Get recent memory context for LLM prompts"""
        try:
            context = {
                'recent_feedback': [],
                'user_preferences': [],
                'task_patterns': []
            }
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get recent feedback
                cursor.execute('''
                    SELECT step, status, notes, timestamp 
                    FROM execution_feedback 
                    ORDER BY created_at DESC 
                    LIMIT ?
                ''', (limit,))
                
                for row in cursor.fetchall():
                    context['recent_feedback'].append({
                        'step': row[0],
                        'status': row[1],
                        'notes': row[2],
                        'timestamp': row[3]
                    })
                
                # Get user preferences
                cursor.execute('''
                    SELECT preference_type, preference_value, confidence 
                    FROM user_preferences 
                    ORDER BY confidence DESC, updated_at DESC
                ''')
                
                for row in cursor.fetchall():
                    context['user_preferences'].append({
                        'type': row[0],
                        'value': row[1],
                        'confidence': row[2]
                    })
                
                # Get task patterns
                cursor.execute('''
                    SELECT task_type, success_rate, total_attempts, common_failures 
                    FROM task_patterns 
                    ORDER BY total_attempts DESC
                ''')
                
                for row in cursor.fetchall():
                    context['task_patterns'].append({
                        'task': row[0],
                        'success_rate': row[1],
                        'total_attempts': row[2],
                        'common_failures': json.loads(row[3]) if row[3] else {}
                    })
            
            return context
            
        except Exception as e:
            self.get_logger().error(f'Error getting memory context: {e}')
            return {}

    def timestamp_to_str(self, timestamp):
        """Convert ROS timestamp to string"""
        return f"{timestamp.sec}.{timestamp.nanosec:09d}"

def main(args=None):
    rclpy.init(args=args)
    node = MemoryNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main() 