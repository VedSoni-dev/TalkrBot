#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from talkrbot_msgs.msg import AACInput, RefinedIntent
from std_msgs.msg import String
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

class UserProfileManager(Node):
    def __init__(self):
        super().__init__('user_profile_manager')
        
        # Subscribe to AAC input to identify user
        self.aac_subscription = self.create_subscription(
            AACInput,
            '/aac_input',
            self.aac_input_callback,
            10
        )
        
        # Subscribe to refined intents to personalize them
        self.intent_subscription = self.create_subscription(
            RefinedIntent,
            '/refined_intent',
            self.intent_callback,
            10
        )
        
        # Publisher for personalized refined intents
        self.personalized_publisher = self.create_publisher(
            RefinedIntent,
            '/refined_intent',
            10
        )
        
        # Publisher for user identification
        self.user_id_publisher = self.create_publisher(
            String,
            '/current_user',
            10
        )
        
        # Load user profiles
        self.profiles = self.load_user_profiles()
        self.current_user = "default"
        self.user_identification_keywords = {
            "vedant": ["vedant", "cold", "blue", "apple juice", "quiet"],
            "sarah": ["sarah", "warm", "red", "tea", "cozy"],
            "alex": ["alex", "coffee", "efficient", "quick", "gray"]
        }
        
        self.get_logger().info('UserProfileManager initialized')
        self.get_logger().info(f'Loaded profiles for: {list(self.profiles.keys())}')
    
    def load_user_profiles(self) -> Dict:
        """Load user profiles from JSON file"""
        try:
            # Get the path to the config file
            package_path = Path(__file__).parent.parent
            config_path = package_path / 'config' / 'user_profiles.json'
            
            if not config_path.exists():
                self.get_logger().error(f'User profiles file not found: {config_path}')
                return {"default": self.get_default_profile()}
            
            with open(config_path, 'r') as f:
                profiles = json.load(f)
            
            self.get_logger().info(f'Successfully loaded {len(profiles)} user profiles')
            return profiles
            
        except Exception as e:
            self.get_logger().error(f'Error loading user profiles: {e}')
            return {"default": self.get_default_profile()}
    
    def get_default_profile(self) -> Dict:
        """Get default user profile"""
        return {
            "likes": ["helpful assistance", "comfort", "reliability"],
            "dislikes": ["confusion", "unreliability"],
            "preferred_drinks": ["water", "juice"],
            "preferred_blankets": ["any available blanket"],
            "default_location": "unknown",
            "comfort_phrases": ["I'm here to help", "Let me assist you"],
            "communication_style": "neutral",
            "temperature_preference": "moderate",
            "accessibility_needs": ["basic assistance"]
        }
    
    def aac_input_callback(self, msg):
        """Process AAC input to identify user and personalize responses"""
        try:
            text = msg.text.lower()
            
            # Try to identify user based on keywords
            identified_user = self.identify_user(text)
            
            if identified_user != self.current_user:
                self.current_user = identified_user
                self.get_logger().info(f'👤 [PROFILE] Identified user: {self.current_user}')
                
                # Publish current user
                user_msg = String()
                user_msg.data = self.current_user
                self.user_id_publisher.publish(user_msg)
            
            # Personalize the input based on user profile
            personalized_text = self.personalize_input(text)
            
            # Create personalized AAC input
            personalized_msg = AACInput()
            personalized_msg.text = personalized_text
            personalized_msg.timestamp = msg.timestamp
            
            self.get_logger().info(f'👤 [PROFILE] Personalized input: "{text}" → "{personalized_text}"')
            
        except Exception as e:
            self.get_logger().error(f'Error processing AAC input: {e}')
    
    def identify_user(self, text: str) -> str:
        """Identify user based on keywords in the text"""
        for user, keywords in self.user_identification_keywords.items():
            if any(keyword in text for keyword in keywords):
                return user
        
        return self.current_user  # Keep current user if no new identification
    
    def personalize_input(self, text: str) -> str:
        """Personalize input based on user preferences"""
        profile = self.profiles.get(self.current_user, self.profiles["default"])
        
        # Add user-specific context to the input
        personalized_parts = [text]
        
        # Add temperature preference for comfort requests
        if any(word in text for word in ["cold", "warm", "temperature", "comfort"]):
            temp_pref = profile.get("temperature_preference", "moderate")
            personalized_parts.append(f"(prefers {temp_pref} temperature)")
        
        # Add location preference
        if "location" not in text and profile.get("default_location") != "unknown":
            default_loc = profile.get("default_location", "unknown")
            personalized_parts.append(f"(default location: {default_loc})")
        
        return " ".join(personalized_parts)
    
    def intent_callback(self, msg):
        """Personalize refined intents based on user profile"""
        try:
            profile = self.profiles.get(self.current_user, self.profiles["default"])
            
            # Create personalized intent
            personalized_msg = RefinedIntent()
            personalized_msg.intent = self.personalize_intent(msg.intent, profile)
            personalized_msg.user_location = self.personalize_location(msg.user_location, profile)
            personalized_msg.priority = msg.priority
            personalized_msg.original_text = msg.original_text
            personalized_msg.timestamp = msg.timestamp
            
            # Publish personalized intent
            self.personalized_publisher.publish(personalized_msg)
            
            self.get_logger().info(f'👤 [PROFILE] Personalized intent: "{msg.intent}" → "{personalized_msg.intent}"')
            self.get_logger().info(f'👤 [PROFILE] Location: "{msg.user_location}" → "{personalized_msg.user_location}"')
            
        except Exception as e:
            self.get_logger().error(f'Error personalizing intent: {e}')
    
    def personalize_intent(self, intent: str, profile: Dict) -> str:
        """Personalize intent based on user preferences"""
        intent_lower = intent.lower()
        
        # Personalize drink requests
        if any(drink in intent_lower for drink in ["water", "drink", "thirsty", "beverage"]):
            preferred_drinks = profile.get("preferred_drinks", ["water"])
            if preferred_drinks:
                return intent.replace("water", preferred_drinks[0]).replace("drink", preferred_drinks[0])
        
        # Personalize blanket requests
        if any(word in intent_lower for word in ["blanket", "cold", "warm", "cover"]):
            preferred_blankets = profile.get("preferred_blankets", ["blanket"])
            if preferred_blankets:
                return intent.replace("blanket", preferred_blankets[0])
        
        # Personalize comfort phrases
        if "help" in intent_lower or "assist" in intent_lower:
            comfort_phrases = profile.get("comfort_phrases", ["I'm here to help"])
            if comfort_phrases:
                return f"{intent} (with {comfort_phrases[0]})"
        
        return intent
    
    def personalize_location(self, location: str, profile: Dict) -> str:
        """Personalize location based on user preferences"""
        if location == "unknown" or location == "default":
            return profile.get("default_location", "unknown")
        return location
    
    def get_user_preferences(self, user_id: str) -> Dict:
        """Get preferences for a specific user"""
        return self.profiles.get(user_id, self.profiles["default"])
    
    def get_communication_style(self, user_id: str) -> str:
        """Get communication style for a specific user"""
        profile = self.profiles.get(user_id, self.profiles["default"])
        return profile.get("communication_style", "neutral")
    
    def get_comfort_phrase(self, user_id: str) -> str:
        """Get a comfort phrase for a specific user"""
        profile = self.profiles.get(user_id, self.profiles["default"])
        comfort_phrases = profile.get("comfort_phrases", ["I'm here to help"])
        return comfort_phrases[0] if comfort_phrases else "I'm here to help"

def main(args=None):
    rclpy.init(args=args)
    node = UserProfileManager()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 