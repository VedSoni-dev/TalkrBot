#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import re

class HistoryQueryNode(Node):
    def __init__(self):
        super().__init__('history_query_node')
        
        # Subscribe to natural language queries
        self.query_subscription = self.create_subscription(
            String,
            '/history_query',
            self.query_callback,
            10
        )
        
        # Publisher for query responses
        self.response_publisher = self.create_publisher(
            String,
            '/history_response',
            10
        )
        
        # Initialize database connection
        self.db_path = self.get_db_path()
        
        self.get_logger().info('HistoryQueryNode initialized')
        self.get_logger().info('Ready to answer questions about task history!')
    
    def get_db_path(self) -> Path:
        """Get the path to the SQLite database"""
        package_path = Path(__file__).parent.parent
        logs_dir = package_path / 'logs'
        return logs_dir / 'task_history.db'
    
    def query_callback(self, msg):
        """Process natural language queries about task history"""
        try:
            query = msg.data.lower()
            self.get_logger().info(f'🔍 [QUERY] Received: "{msg.data}"')
            
            # Parse the query and generate response
            response = self.process_query(query)
            
            # Publish response
            response_msg = String()
            response_msg.data = response
            self.response_publisher.publish(response_msg)
            
            self.get_logger().info(f'💬 [RESPONSE] {response}')
            
        except Exception as e:
            self.get_logger().error(f'Error processing query: {e}')
            response_msg = String()
            response_msg.data = f"Sorry, I couldn't process that query: {str(e)}"
            self.response_publisher.publish(response_msg)
    
    def process_query(self, query: str) -> str:
        """Process natural language query and return response"""
        
        # Check for "did I already" questions
        if "did i already" in query or "have i already" in query:
            return self.handle_completion_query(query)
        
        # Check for "when did i" questions
        elif "when did i" in query or "when was" in query:
            return self.handle_timing_query(query)
        
        # Check for "how many" questions
        elif "how many" in query:
            return self.handle_count_query(query)
        
        # Check for "what failed" questions
        elif "failed" in query or "failure" in query:
            return self.handle_failure_query(query)
        
        # Check for "summary" or "overview" requests
        elif "summary" in query or "overview" in query or "today" in query:
            return self.handle_summary_query(query)
        
        # Default response
        else:
            return self.handle_general_query(query)
    
    def handle_completion_query(self, query: str) -> str:
        """Handle questions about whether tasks were completed"""
        try:
            # Extract task from query
            task = self.extract_task_from_query(query)
            if not task:
                return "I couldn't understand what task you're asking about. Could you be more specific?"
            
            # Check recent history (last 24 hours)
            recent_tasks = self.get_recent_tasks_by_intent(task, hours=24)
            
            if not recent_tasks:
                return f"No, I haven't completed '{task}' recently."
            
            # Check if any were successful
            successful = [t for t in recent_tasks if t['status'] == 'success']
            failed = [t for t in recent_tasks if t['status'] == 'failure']
            
            if successful:
                latest = successful[0]
                return f"Yes! I successfully completed '{task}' at {latest['timestamp']}."
            elif failed:
                latest = failed[0]
                return f"I tried to complete '{task}' at {latest['timestamp']}, but it failed: {latest.get('reason', 'unknown reason')}."
            else:
                return f"I have a record of '{task}' but I'm not sure about the status."
                
        except Exception as e:
            return f"Sorry, I couldn't check that for you: {str(e)}"
    
    def handle_timing_query(self, query: str) -> str:
        """Handle questions about when tasks were performed"""
        try:
            task = self.extract_task_from_query(query)
            if not task:
                return "I couldn't understand what task you're asking about."
            
            recent_tasks = self.get_recent_tasks_by_intent(task, hours=168)  # Last week
            
            if not recent_tasks:
                return f"I haven't performed '{task}' recently."
            
            latest = recent_tasks[0]
            return f"I last performed '{task}' at {latest['timestamp']} with status: {latest['status']}."
            
        except Exception as e:
            return f"Sorry, I couldn't find that information: {str(e)}"
    
    def handle_count_query(self, query: str) -> str:
        """Handle questions about task counts"""
        try:
            if "successful" in query or "succeeded" in query:
                count = self.get_task_count(status="success")
                return f"I have successfully completed {count} tasks."
            elif "failed" in query or "failure" in query:
                count = self.get_task_count(status="failure")
                return f"I have failed {count} tasks."
            else:
                count = self.get_task_count()
                return f"I have attempted {count} tasks total."
                
        except Exception as e:
            return f"Sorry, I couldn't count that for you: {str(e)}"
    
    def handle_failure_query(self, query: str) -> str:
        """Handle questions about failures"""
        try:
            recent_failures = self.get_recent_tasks(status="failure", hours=24)
            
            if not recent_failures:
                return "I haven't had any failures recently!"
            
            if len(recent_failures) == 1:
                failure = recent_failures[0]
                return f"My most recent failure was '{failure['intent']}' at {failure['timestamp']}: {failure.get('reason', 'unknown reason')}."
            else:
                failure_list = [f"'{f['intent']}' ({f.get('reason', 'unknown')})" for f in recent_failures[:3]]
                return f"I've had {len(recent_failures)} recent failures: {', '.join(failure_list)}."
                
        except Exception as e:
            return f"Sorry, I couldn't check my failures: {str(e)}"
    
    def handle_summary_query(self, query: str) -> str:
        """Handle summary requests"""
        try:
            hours = 24 if "today" in query else 168  # Default to week
            recent_tasks = self.get_recent_tasks(hours=hours)
            
            if not recent_tasks:
                return f"I haven't performed any tasks in the last {hours} hours."
            
            successful = [t for t in recent_tasks if t['status'] == 'success']
            failed = [t for t in recent_tasks if t['status'] == 'failure']
            
            success_rate = len(successful) / len(recent_tasks) * 100 if recent_tasks else 0
            
            return f"Summary of the last {hours} hours: {len(recent_tasks)} total tasks, {len(successful)} successful, {len(failed)} failed. Success rate: {success_rate:.1f}%."
            
        except Exception as e:
            return f"Sorry, I couldn't generate a summary: {str(e)}"
    
    def handle_general_query(self, query: str) -> str:
        """Handle general queries"""
        return "I can answer questions about what tasks I've completed, when I did them, how many I've attempted, and what failures I've had. Try asking something like 'Did I already bring the blanket today?' or 'How many tasks have I completed?'"
    
    def extract_task_from_query(self, query: str) -> Optional[str]:
        """Extract task name from natural language query"""
        # Common patterns for task extraction
        patterns = [
            r"bring\s+(\w+)",
            r"get\s+(\w+)",
            r"turn\s+(\w+)",
            r"open\s+(\w+)",
            r"close\s+(\w+)",
            r"(\w+)\s+blanket",
            r"(\w+)\s+water",
            r"(\w+)\s+juice",
            r"(\w+)\s+tea",
            r"(\w+)\s+lights"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, query)
            if match:
                return match.group(1)
        
        return None
    
    def get_recent_tasks(self, user: str = None, status: str = None, hours: int = 24) -> List[Dict]:
        """Get recent tasks with optional filters"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = '''
                    SELECT timestamp, user, intent, status, location, reason, details
                    FROM task_history 
                    WHERE timestamp > datetime('now', '-{} hours')
                '''.format(hours)
                
                params = []
                
                if user:
                    query += ' AND user = ?'
                    params.append(user)
                
                if status:
                    query += ' AND status = ?'
                    params.append(status)
                
                query += ' ORDER BY timestamp DESC'
                
                cursor.execute(query, params)
                
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
    
    def get_recent_tasks_by_intent(self, intent: str, hours: int = 24) -> List[Dict]:
        """Get recent tasks by specific intent"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT timestamp, user, intent, status, location, reason, details
                    FROM task_history 
                    WHERE intent LIKE ? AND timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp DESC
                '''.format(hours), (f'%{intent}%',))
                
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
            self.get_logger().error(f'Error getting tasks by intent: {e}')
            return []
    
    def get_task_count(self, status: str = None) -> int:
        """Get count of tasks with optional status filter"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = 'SELECT COUNT(*) FROM task_history'
                params = []
                
                if status:
                    query += ' WHERE status = ?'
                    params.append(status)
                
                cursor.execute(query, params)
                return cursor.fetchone()[0]
                
        except Exception as e:
            self.get_logger().error(f'Error getting task count: {e}')
            return 0

def main(args=None):
    rclpy.init(args=args)
    node = HistoryQueryNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 