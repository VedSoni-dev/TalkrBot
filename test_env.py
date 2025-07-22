#!/usr/bin/env python3
"""
Test script to verify GEMINI_API_KEY is loaded correctly
"""

import os
from dotenv import load_dotenv

def test_env_loading():
    print("=== Testing Environment Variable Loading ===")
    
    # Test 1: Check system environment
    sys_key = os.getenv('GEMINI_API_KEY')
    print(f"System env GEMINI_API_KEY: {sys_key[:10] + '...' if sys_key and len(sys_key) > 10 else sys_key}")
    
    # Test 2: Load from .env file
    load_dotenv()
    dotenv_key = os.getenv('GEMINI_API_KEY')
    print(f"After load_dotenv() GEMINI_API_KEY: {dotenv_key[:10] + '...' if dotenv_key and len(dotenv_key) > 10 else dotenv_key}")
    
    # Test 3: Check if they match
    if sys_key == dotenv_key:
        print("✅ System env and .env file match!")
    else:
        print("⚠️  System env and .env file differ")
    
    # Test 4: Check if it's not the placeholder
    if dotenv_key and dotenv_key != "YOUR_ACTUAL_GEMINI_API_KEY_HERE":
        print("✅ API key is properly set (not placeholder)")
    else:
        print("❌ API key is still the placeholder value")

if __name__ == "__main__":
    test_env_loading()
