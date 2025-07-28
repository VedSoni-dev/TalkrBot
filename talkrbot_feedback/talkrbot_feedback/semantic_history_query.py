#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

class SemanticHistoryQueryNode(Node):
    def __init__(self):
        super().__init__('semantic_history_query_node')
        
        # Subscribe to semantic queries
        self.query_subscription = self.create_subscription(
            String,
            '/semantic_history_query',
            self.query_callback,
            10
        )
        
        # Publisher for semantic responses
        self.response_publisher = self.create_publisher(
            String,
            '/semantic_history_response',
            10
        )
        
        # Initialize database connection
        self.db_path = self.get_db_path()
        
        # Initialize TF-IDF vectorizer for semantic similarity
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=1000
        )
        
        # Cache for task embeddings
        self.task_embeddings = None
        self.task_texts = []
        self.task_data = []
        
        # Load and prepare task data
        self.load_task_data()
        
        self.get_logger().info('SemanticHistoryQueryNode initialized')
        self.get_logger().info('Ready to answer semantic questions about task history!')
    
    def get_db_path(self) -> Path:
        """Get the path to the SQLite database"""
        package_path = Path(__file__).parent.parent
        logs_dir = package_path / 'logs'
        return logs_dir / 'task_history.db'
    
    def load_task_data(self):
        """Load task data and prepare embeddings"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT timestamp, user, intent, status, location, reason, details
                    FROM task_history 
                    ORDER BY timestamp DESC
                ''')
                
                tasks = []
                task_texts = []
                
                for row in cursor.fetchall():
                    task = {
                        'timestamp': row[0],
                        'user': row[1],
                        'intent': row[2],
                        'status': row[3],
                        'location': row[4],
                        'reason': row[5],
                        'details': row[6]
                    }
                    tasks.append(task)
                    
                    # Create rich text representation for semantic search
                    task_text = self.create_task_text(task)
                    task_texts.append(task_text)
                
                self.task_data = tasks
                self.task_texts = task_texts
                
                # Create TF-IDF embeddings
                if task_texts:
                    self.task_embeddings = self.vectorizer.fit_transform(task_texts)
                
                self.get_logger().info(f'Loaded {len(tasks)} tasks for semantic search')
                
        except Exception as e:
            self.get_logger().error(f'Error loading task data: {e}')
            self.task_data = []
            self.task_texts = []
            self.task_embeddings = None
    
    def create_task_text(self, task: Dict) -> str:
        """Create rich text representation of a task for semantic search"""
        text_parts = []
        
        # Add intent
        text_parts.append(f"task: {task['intent']}")
        
        # Add status
        text_parts.append(f"status: {task['status']}")
        
        # Add location if available
        if task.get('location') and task['location'] != 'unknown':
            text_parts.append(f"location: {task['location']}")
        
        # Add details if available
        if task.get('details'):
            text_parts.append(f"details: {task['details']}")
        
        # Add reason if it's a failure
        if task['status'] == 'failure' and task.get('reason'):
            text_parts.append(f"reason: {task['reason']}")
        
        # Add user
        text_parts.append(f"user: {task['user']}")
        
        # Add time context
        try:
            dt = datetime.fromisoformat(task['timestamp'].replace('Z', '+00:00'))
            text_parts.append(f"time: {dt.strftime('%I:%M %p')}")
            text_parts.append(f"day: {dt.strftime('%A')}")
        except:
            pass
        
        return " ".join(text_parts)
    
    def query_callback(self, msg):
        """Process semantic queries about task history"""
        try:
            query = msg.data
            self.get_logger().info(f'🧠 [SEMANTIC QUERY] Received: "{query}"')
            
            # Process the semantic query
            response = self.process_semantic_query(query)
            
            # Publish response
            response_msg = String()
            response_msg.data = response
            self.response_publisher.publish(response_msg)
            
            self.get_logger().info(f'💬 [SEMANTIC RESPONSE] {response}')
            
        except Exception as e:
            self.get_logger().error(f'Error processing semantic query: {e}')
            response_msg = String()
            response_msg.data = f"Sorry, I couldn't process that semantic query: {str(e)}"
            self.response_publisher.publish(response_msg)
    
    def process_semantic_query(self, query: str) -> str:
        """Process semantic query and return natural language response"""
        query_lower = query.lower()
        
        # Check for time-based queries
        if any(word in query_lower for word in ['today', 'yesterday', 'this week', 'morning', 'afternoon', 'evening']):
            return self.handle_time_based_query(query)
        
        # Check for activity-based queries
        elif any(word in query_lower for word in ['what did', 'what have', 'what was', 'activities', 'tasks']):
            return self.handle_activity_query(query)
        
        # Check for status-based queries
        elif any(word in query_lower for word in ['successful', 'failed', 'problems', 'issues', 'worked', 'didn\'t work']):
            return self.handle_status_query(query)
        
        # Check for location-based queries
        elif any(word in query_lower for word in ['kitchen', 'living room', 'bedroom', 'office', 'where']):
            return self.handle_location_query(query)
        
        # Check for user-specific queries
        elif any(word in query_lower for word in ['vedant', 'sarah', 'alex', 'my', 'for me']):
            return self.handle_user_query(query)
        
        # Default to semantic search
        else:
            return self.handle_semantic_search(query)
    
    def handle_time_based_query(self, query: str) -> str:
        """Handle queries about specific time periods"""
        query_lower = query.lower()
        
        # Determine time period
        if 'today' in query_lower:
            hours = 24
            period = "today"
        elif 'yesterday' in query_lower:
            hours = 48
            period = "yesterday"
        elif 'this week' in query_lower:
            hours = 168
            period = "this week"
        elif 'morning' in query_lower:
            hours = 12
            period = "this morning"
        elif 'afternoon' in query_lower:
            hours = 6
            period = "this afternoon"
        elif 'evening' in query_lower:
            hours = 6
            period = "this evening"
        else:
            hours = 24
            period = "recently"
        
        # Get tasks for the time period
        tasks = self.get_tasks_by_time_period(hours)
        
        if not tasks:
            return f"I haven't performed any tasks {period}."
        
        # Generate natural language summary
        return self.generate_time_summary(tasks, period)
    
    def handle_activity_query(self, query: str) -> str:
        """Handle queries about activities and tasks"""
        # Use semantic search to find relevant tasks
        relevant_tasks = self.semantic_search(query, top_k=5)
        
        if not relevant_tasks:
            return "I haven't found any activities matching your query."
        
        # Generate natural language response
        return self.generate_activity_summary(relevant_tasks, query)
    
    def handle_status_query(self, query: str) -> str:
        """Handle queries about success/failure status"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['successful', 'worked', 'good', 'well']):
            tasks = self.get_tasks_by_status('success')
            if tasks:
                return self.generate_success_summary(tasks)
            else:
                return "I haven't had any successful tasks recently."
        
        elif any(word in query_lower for word in ['failed', 'problems', 'issues', 'didn\'t work', 'wrong']):
            tasks = self.get_tasks_by_status('failure')
            if tasks:
                return self.generate_failure_summary(tasks)
            else:
                return "I haven't had any failures recently!"
        
        else:
            return self.handle_semantic_search(query)
    
    def handle_location_query(self, query: str) -> str:
        """Handle queries about specific locations"""
        # Extract location from query
        locations = ['kitchen', 'living room', 'bedroom', 'office', 'bathroom']
        found_location = None
        
        for location in locations:
            if location in query.lower():
                found_location = location
                break
        
        if found_location:
            tasks = self.get_tasks_by_location(found_location)
            if tasks:
                return self.generate_location_summary(tasks, found_location)
            else:
                return f"I haven't performed any tasks in the {found_location} recently."
        else:
            return self.handle_semantic_search(query)
    
    def handle_user_query(self, query: str) -> str:
        """Handle user-specific queries"""
        # Extract user from query
        users = ['vedant', 'sarah', 'alex']
        found_user = None
        
        for user in users:
            if user in query.lower():
                found_user = user
                break
        
        if found_user:
            tasks = self.get_tasks_by_user(found_user)
            if tasks:
                return self.generate_user_summary(tasks, found_user)
            else:
                return f"I haven't performed any tasks for {found_user} recently."
        else:
            # Assume current user if "my" or "for me" is mentioned
            if any(word in query.lower() for word in ['my', 'for me']):
                tasks = self.get_tasks_by_user('vedant')  # Default user
                if tasks:
                    return self.generate_user_summary(tasks, 'you')
                else:
                    return "I haven't performed any tasks for you recently."
            else:
                return self.handle_semantic_search(query)
    
    def handle_semantic_search(self, query: str) -> str:
        """Handle general semantic search queries"""
        relevant_tasks = self.semantic_search(query, top_k=3)
        
        if not relevant_tasks:
            return "I couldn't find any tasks matching your query. Could you be more specific?"
        
        return self.generate_semantic_summary(relevant_tasks, query)
    
    def semantic_search(self, query: str, top_k: int = 3) -> List[Tuple[Dict, float]]:
        """Perform semantic search using TF-IDF and cosine similarity"""
        if not self.task_embeddings or not self.task_texts:
            return []
        
        try:
            # Transform query
            query_vector = self.vectorizer.transform([query])
            
            # Calculate similarities
            similarities = cosine_similarity(query_vector, self.task_embeddings).flatten()
            
            # Get top-k results
            top_indices = similarities.argsort()[-top_k:][::-1]
            
            results = []
            for idx in top_indices:
                if float(similarities[idx]) > 0.1:  # Minimum similarity threshold
                    results.append((self.task_data[idx], float(similarities[idx])))
            
            return results
            
        except Exception as e:
            self.get_logger().error(f'Error in semantic search: {e}')
            return []
    
    def get_tasks_by_time_period(self, hours: int) -> List[Dict]:
        """Get tasks from the last N hours"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT timestamp, user, intent, status, location, reason, details
                    FROM task_history 
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp DESC
                '''.format(hours))
                
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
            self.get_logger().error(f'Error getting tasks by time: {e}')
            return []
    
    def get_tasks_by_status(self, status: str) -> List[Dict]:
        """Get tasks by status"""
        return [task for task in self.task_data if task['status'] == status]
    
    def get_tasks_by_location(self, location: str) -> List[Dict]:
        """Get tasks by location"""
        return [task for task in self.task_data if task.get('location') == location]
    
    def get_tasks_by_user(self, user: str) -> List[Dict]:
        """Get tasks by user"""
        return [task for task in self.task_data if task['user'] == user]
    
    def generate_time_summary(self, tasks: List[Dict], period: str) -> str:
        """Generate natural language summary for time-based queries"""
        if not tasks:
            return f"I haven't performed any tasks {period}."
        
        # Group by status
        successful = [t for t in tasks if t['status'] == 'success']
        failed = [t for t in tasks if t['status'] == 'failure']
        
        summary_parts = []
        
        if successful:
            task_descriptions = []
            for task in successful[:3]:  # Limit to 3 most recent
                time_str = self.format_time(task['timestamp'])
                task_descriptions.append(f"{task['intent']} at {time_str}")
            
            if len(task_descriptions) == 1:
                summary_parts.append(f"I {task_descriptions[0]}.")
            else:
                summary_parts.append(f"I {', '.join(task_descriptions[:-1])}, and {task_descriptions[-1]}.")
        
        if failed:
            task_descriptions = []
            for task in failed[:2]:  # Limit to 2 most recent failures
                time_str = self.format_time(task['timestamp'])
                reason = task.get('reason', 'unknown reason')
                task_descriptions.append(f"tried to {task['intent']} at {time_str} but failed because {reason}")
            
            if task_descriptions:
                summary_parts.append(f"I also {', '.join(task_descriptions)}.")
        
        return " ".join(summary_parts)
    
    def generate_activity_summary(self, tasks: List[Tuple[Dict, float]], query: str) -> str:
        """Generate summary for activity queries"""
        if not tasks:
            return "I haven't found any activities matching your query."
        
        task_descriptions = []
        for task, similarity in tasks:
            time_str = self.format_time(task['timestamp'])
            status_emoji = "✅" if task['status'] == 'success' else "❌"
            task_descriptions.append(f"{status_emoji} {task['intent']} at {time_str}")
        
        return f"Based on your query '{query}', here's what I found: {'; '.join(task_descriptions)}."
    
    def generate_success_summary(self, tasks: List[Dict]) -> str:
        """Generate summary for successful tasks"""
        if not tasks:
            return "I haven't had any successful tasks recently."
        
        recent_tasks = tasks[:3]
        task_descriptions = []
        
        for task in recent_tasks:
            time_str = self.format_time(task['timestamp'])
            task_descriptions.append(f"{task['intent']} at {time_str}")
        
        return f"My recent successful tasks include: {', '.join(task_descriptions)}."
    
    def generate_failure_summary(self, tasks: List[Dict]) -> str:
        """Generate summary for failed tasks"""
        if not tasks:
            return "I haven't had any failures recently!"
        
        recent_tasks = tasks[:2]
        task_descriptions = []
        
        for task in recent_tasks:
            time_str = self.format_time(task['timestamp'])
            reason = task.get('reason', 'unknown reason')
            task_descriptions.append(f"{task['intent']} at {time_str} (reason: {reason})")
        
        return f"My recent failures were: {', '.join(task_descriptions)}."
    
    def generate_location_summary(self, tasks: List[Dict], location: str) -> str:
        """Generate summary for location-based queries"""
        if not tasks:
            return f"I haven't performed any tasks in the {location} recently."
        
        recent_tasks = tasks[:3]
        task_descriptions = []
        
        for task in recent_tasks:
            time_str = self.format_time(task['timestamp'])
            status_emoji = "✅" if task['status'] == 'success' else "❌"
            task_descriptions.append(f"{status_emoji} {task['intent']} at {time_str}")
        
        return f"In the {location}, I've: {'; '.join(task_descriptions)}."
    
    def generate_user_summary(self, tasks: List[Dict], user: str) -> str:
        """Generate summary for user-specific queries"""
        if not tasks:
            return f"I haven't performed any tasks for {user} recently."
        
        recent_tasks = tasks[:3]
        task_descriptions = []
        
        for task in recent_tasks:
            time_str = self.format_time(task['timestamp'])
            status_emoji = "✅" if task['status'] == 'success' else "❌"
            task_descriptions.append(f"{status_emoji} {task['intent']} at {time_str}")
        
        return f"For {user}, I've: {'; '.join(task_descriptions)}."
    
    def generate_semantic_summary(self, tasks: List[Tuple[Dict, float]], query: str) -> str:
        """Generate summary for semantic search results"""
        if not tasks:
            return "I couldn't find any tasks matching your query."
        
        task_descriptions = []
        for task, similarity in tasks:
            time_str = self.format_time(task['timestamp'])
            status_emoji = "✅" if task['status'] == 'success' else "❌"
            task_descriptions.append(f"{status_emoji} {task['intent']} at {time_str}")
        
        return f"Based on your query '{query}', I found: {'; '.join(task_descriptions)}."
    
    def format_time(self, timestamp: str) -> str:
        """Format timestamp for natural language output"""
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return "unknown time"

def main(args=None):
    rclpy.init(args=args)
    node = SemanticHistoryQueryNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 