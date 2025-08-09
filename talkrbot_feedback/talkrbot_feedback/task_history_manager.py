#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import ExecutionFeedback, RefinedIntent
from std_msgs.msg import String
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import sqlite3

class TaskHistoryManager(Node):
    def __init__(self):
        super().__init__('task_history_manager')
        
        # Subscribe to execution feedback to track task completion
        self.feedback_subscription = self.create_subscription(
            ExecutionFeedback,
            '/execution_feedback',
            self.feedback_callback,
            10
        )
        
        # Subscribe to refined intents to track what was attempted
        self.intent_subscription = self.create_subscription(
            RefinedIntent,
            '/refined_intent',
            self.intent_callback,
            10
        )
        
        # Subscribe to current user for context
        self.user_subscription = self.create_subscription(
            String,
            '/current_user',
            self.user_callback,
            10
        )
        
        # Publisher for task history queries
        self.history_publisher = self.create_publisher(
            String,
            '/task_history',
            10
        )
        
        # Initialize task history
        self.task_history = []
        self.current_user = "default"
        self.current_intent = None
        self.history_file = self.get_history_file_path()
        
        # Load existing history
        self.load_task_history()
        
        # Initialize SQLite database for better querying
        self.db_path = self.get_db_path()
        self.init_database()
        
        self.get_logger().info('TaskHistoryManager initialized')
        self.get_logger().info(f'Loaded {len(self.task_history)} historical tasks')
    
    def get_history_file_path(self) -> Path:
        """Get the path to the task history JSON file"""
        package_path = Path(__file__).parent.parent
        logs_dir = package_path / 'logs'
        logs_dir.mkdir(exist_ok=True)
        return logs_dir / 'task_history.json'
    
    def get_db_path(self) -> Path:
        """Get the path to the SQLite database"""
        package_path = Path(__file__).parent.parent
        logs_dir = package_path / 'logs'
        logs_dir.mkdir(exist_ok=True)
        return logs_dir / 'task_history.db'
    
    def init_database(self):
        """Initialize SQLite database for task history"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS task_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        user TEXT NOT NULL,
                        intent TEXT NOT NULL,
                        status TEXT NOT NULL,
                        location TEXT,
                        reason TEXT,
                        details TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create indexes for better querying
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_user ON task_history(user)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_status ON task_history(status)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON task_history(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_intent ON task_history(intent)')
                
                conn.commit()
                
            self.get_logger().info(f'Initialized task history database: {self.db_path}')
            
        except Exception as e:
            self.get_logger().error(f'Error initializing database: {e}')
    
    def load_task_history(self):
        """Load existing task history from JSON file"""
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r') as f:
                    self.task_history = json.load(f)
                self.get_logger().info(f'Loaded {len(self.task_history)} tasks from history file')
            else:
                self.task_history = []
                self.get_logger().info('No existing history file found, starting fresh')
                
        except Exception as e:
            self.get_logger().error(f'Error loading task history: {e}')
            self.task_history = []
    
    def save_task_history(self):
        """Save task history to JSON file"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.task_history, f, indent=2)
            self.get_logger().debug('Task history saved to file')
        except Exception as e:
            self.get_logger().error(f'Error saving task history: {e}')
    
    def add_task_to_db(self, task_data: Dict):
        """Add task to SQLite database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO task_history 
                    (timestamp, user, intent, status, location, reason, details)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    task_data.get('timestamp'),
                    task_data.get('user'),
                    task_data.get('intent'),
                    task_data.get('status'),
                    task_data.get('location'),
                    task_data.get('reason'),
                    task_data.get('details')
                ))
                conn.commit()
                
        except Exception as e:
            self.get_logger().error(f'Error adding task to database: {e}')
    
    def user_callback(self, msg):
        """Track current user"""
        self.current_user = msg.data
        self.get_logger().debug(f'Current user: {self.current_user}')
    
    def intent_callback(self, msg):
        """Track current intent being processed"""
        self.current_intent = {
            'intent': msg.intent,
            'user_location': msg.user_location,
            'priority': msg.priority,
            'original_text': msg.original_text
        }
        self.get_logger().debug(f'Tracking intent: {msg.intent}')
    
    def feedback_callback(self, msg):
        """Process execution feedback and log task history"""
        try:
            # Create task history entry
            task_entry = {
                'timestamp': datetime.now().isoformat(),
                'user': self.current_user,
                'intent': msg.step,
                'status': msg.status,
                'location': self.current_intent.get('user_location', 'unknown') if self.current_intent else 'unknown',
                'details': msg.notes
            }
            
            # Add failure reason if applicable
            if msg.status == 'failure':
                task_entry['reason'] = msg.notes
            
            # Add to memory
            self.task_history.append(task_entry)
            self.add_task_to_db(task_entry)
            
            # Save to file
            self.save_task_history()
            
            # Log the task
            status_emoji = "✅" if msg.status == "success" else "❌"
            self.get_logger().info(f'{status_emoji} [HISTORY] Logged task: {msg.step} ({msg.status}) for {self.current_user}')
            
            # Check for patterns and provide insights
            self.analyze_patterns()
            
        except Exception as e:
            self.get_logger().error(f'Error processing feedback: {e}')
    
    def analyze_patterns(self):
        """Analyze task patterns and provide insights"""
        try:
            # Get recent tasks for current user
            recent_tasks = self.get_recent_tasks(self.current_user, hours=24)
            
            # Check for repeated failures
            recent_failures = [task for task in recent_tasks if task['status'] == 'failure']
            if recent_failures:
                self.get_logger().info(f'⚠️ [PATTERN] {len(recent_failures)} recent failures for {self.current_user}')
                
                # Check for specific failure patterns
                failure_reasons = {}
                for task in recent_failures:
                    reason = task.get('reason', 'unknown')
                    failure_reasons[reason] = failure_reasons.get(reason, 0) + 1
                
                for reason, count in failure_reasons.items():
                    if count > 1:
                        self.get_logger().info(f'🔄 [PATTERN] Repeated failure: {reason} ({count} times)')
            
            # Check for successful patterns
            recent_successes = [task for task in recent_tasks if task['status'] == 'success']
            if recent_successes:
                self.get_logger().info(f'✅ [PATTERN] {len(recent_successes)} recent successes for {self.current_user}')
                
        except Exception as e:
            self.get_logger().error(f'Error analyzing patterns: {e}')
    
    def get_recent_tasks(self, user: str, hours: int = 24) -> List[Dict]:
        """Get recent tasks for a specific user"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT timestamp, user, intent, status, location, reason, details
                    FROM task_history 
                    WHERE user = ? AND timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp DESC
                '''.format(hours), (user,))
                
                tasks = []
                for row in cursor.fetchall():
                    tasks.append({
                        'timestamp': row[0],
                        'user': row[1],
                        'intent': row[2],
                        'status': row[3],
                        'location': row[4],
                        'reason': row[5],
                        'details': row[6]
                    })
                
                return tasks
                
        except Exception as e:
            self.get_logger().error(f'Error getting recent tasks: {e}')
            return []
    
    def get_task_summary(self, user: str, hours: int = 24) -> Dict:
        """Get a summary of tasks for a user"""
        try:
            recent_tasks = self.get_recent_tasks(user, hours)
            
            summary = {
                'user': user,
                'total_tasks': len(recent_tasks),
                'successful_tasks': len([t for t in recent_tasks if t['status'] == 'success']),
                'failed_tasks': len([t for t in recent_tasks if t['status'] == 'failure']),
                'success_rate': 0.0,
                'common_intents': {},
                'failure_patterns': {}
            }
            
            if summary['total_tasks'] > 0:
                summary['success_rate'] = summary['successful_tasks'] / summary['total_tasks']
            
            # Analyze common intents
            for task in recent_tasks:
                intent = task['intent']
                summary['common_intents'][intent] = summary['common_intents'].get(intent, 0) + 1
            
            # Analyze failure patterns
            for task in recent_tasks:
                if task['status'] == 'failure':
                    reason = task.get('reason', 'unknown')
                    summary['failure_patterns'][reason] = summary['failure_patterns'].get(reason, 0) + 1
            
            return summary
            
        except Exception as e:
            self.get_logger().error(f'Error getting task summary: {e}')
            return {}
    
    def has_recent_task(self, user: str, intent: str, hours: int = 24) -> bool:
        """Check if user has recently attempted a specific task"""
        try:
            recent_tasks = self.get_recent_tasks(user, hours)
            return any(task['intent'] == intent for task in recent_tasks)
        except Exception as e:
            self.get_logger().error(f'Error checking recent task: {e}')
            return False
    
    def get_last_failure_reason(self, user: str, intent: str) -> Optional[str]:
        """Get the reason for the last failure of a specific task"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT reason FROM task_history 
                    WHERE user = ? AND intent = ? AND status = 'failure'
                    ORDER BY timestamp DESC LIMIT 1
                ''', (user, intent))
                
                result = cursor.fetchone()
                return result[0] if result else None
                
        except Exception as e:
            self.get_logger().error(f'Error getting last failure reason: {e}')
            return None

def main(args=None):
    rclpy.init(args=args)
    node = TaskHistoryManager()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main() 