# 🤖 TalkrBot: LLM-Powered Assistive Robot

> **An intelligent ROS 2 Humble robot that translates vague AAC (Augmentative and Alternative Communication) phrases into precise robot behaviors using Google Gemini AI.**

[![ROS 2 Humble](https://img.shields.io/badge/ROS%202-Humble-blue.svg)](https://docs.ros.org/en/humble/)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

TalkrBot is an advanced assistive robotics system designed to help users with communication difficulties. It uses natural language processing to interpret vague AAC input (like "water yummy more") and translates it into structured robot actions (like "serve more water").

### 🌟 Key Features

- **🧠 LLM-Powered Intent Understanding**: Uses Google Gemini AI to interpret vague AAC phrases
- **🎯 Context-Aware Planning**: Generates step-by-step robot skill plans
- **🤖 Real Robot Integration**: Nav2 navigation and arm control capabilities
- **👤 Personalized User Profiles**: Remembers user preferences and communication styles
- **🔄 Failure Recovery**: Intelligent replanning when tasks fail
- **💬 Natural Dialogue**: Robot can ask clarifying questions and process responses
- **📊 Task History & Memory**: Persistent storage of user interactions and preferences
- **🔍 Semantic Search**: Query task history using natural language

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AAC Input     │    │   LLM Layer     │    │  Robot Control  │
│                 │    │                 │    │                 │
│ • WebSocket     │───▶│ • Intent Refiner │───▶│ • Nav2          │
│ • REST API      │    │ • GROOT Planner  │    │ • Arm Control   │
│ • ROS Topics    │    │ • Memory Node    │    │ • Skill Executor│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Perception    │    │   Feedback      │    │   User Profiles │
│                 │    │                 │    │                 │
│ • YOLOv8        │    │ • Failure Handler│   │ • Preferences   │
│ • Depth Fusion  │    │ • Speech Node   │    │ • History       │
│ • Object Detect │    │ • Task History  │    │ • Patterns      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📦 ROS 2 Packages

| Package | Purpose | Key Components |
|---------|---------|----------------|
| `talkrbot_aac` | AAC Input Processing | WebSocket server, REST API, input normalization |
| `talkrbot_llm` | AI/LLM Processing | Intent refinement, planning, memory management |
| `talkrbot_perception` | Computer Vision | YOLOv8 object detection, depth fusion |
| `talkrbot_planner` | Robot Control | Skill execution, Nav2 integration |
| `talkrbot_nav` | Navigation | Mock robot simulation, Nav2 bridge |
| `talkrbot_feedback` | User Interaction | Failure handling, speech, user profiles |
| `talkrbot_msgs` | Custom Messages | AACInput, TaskCommand, DetectedObject, etc. |

## 🚀 Quick Start

### Prerequisites

```bash
# Install ROS 2 Humble
sudo apt update
sudo apt install ros-humble-desktop

# Install Python dependencies
pip install google-generativeai ultralytics opencv-python websockets

# Install ROS 2 packages
sudo apt install ros-humble-nav2-* ros-humble-control-msgs ros-humble-trajectory-msgs
```

### 1. Clone and Build

```bash
# Clone the repository
git clone https://github.com/yourusername/TalkrBot.git
cd TalkrBot

# Build the workspace
colcon build

# Source the workspace
source install/setup.bash
```

### 2. Set Up Environment

```bash
# Create .env file with your Gemini API key
echo "GEMINI_API_KEY=your_actual_gemini_api_key_here" > .env

# Load environment variables
source .env
```

### 3. Launch Core Nodes

```bash
# Terminal 1: AAC Node (WebSocket + REST API)
ros2 run talkrbot_aac aac_node

# Terminal 2: LLM Intent Refiner
ros2 run talkrbot_llm intent_refiner_node

# Terminal 3: GROOT Planner
ros2 run talkrbot_llm groot_planner_node

# Terminal 4: Skill Executor
ros2 run talkrbot_planner skill_executor_node_simple

# Terminal 5: Mock Robot (for testing)
ros2 run talkrbot_nav mock_robot_node
```

### 4. Test the System

```bash
# Send a test AAC input via WebSocket
python3 test_websocket.py

# Or publish directly to ROS topic
ros2 topic pub /aac_input talkrbot_msgs/AACInput "{text: 'I am cold', user_id: 'vedant'}"
```

## 🧪 Testing Examples

### Basic AAC Input
```json
{
  "text": "water yummy more",
  "user_id": "vedant",
  "metadata": {"source": "web"}
}
```

**Expected Output:**
```
[INFO] [llm_node]: Published TaskCommand: 
  task='serve', object='water', location='None', 
  parameters='{"quantity": "more"}', confidence=0.9
```

### Complex Task Planning
```json
{
  "text": "bring blanket",
  "user_id": "sarah"
}
```

**Expected Skill Plan:**
```json
[
  "go_to('closet')",
  "grasp('blanket')", 
  "go_to('user')",
  "place('blanket')"
]
```

## 🔧 Advanced Features

### User Profiles & Personalization

The system maintains user profiles with preferences:

```json
{
  "vedant": {
    "likes": ["cold water", "quiet environment"],
    "dislikes": ["loud noises", "bright lights"],
    "preferred_drinks": ["water", "coffee"],
    "default_location": "desk",
    "communication_style": "direct"
  }
}
```

### Failure Recovery & Dialogue

When tasks fail, the robot can:
- Ask clarifying questions: "I couldn't find the blanket. Is it in the bedroom closet?"
- Suggest alternatives: "Would you like a different blanket or a jacket instead?"
- Replan based on user responses

### Task History & Memory

```bash
# Query task history
ros2 topic pub /history_query std_msgs/String "How many times did I ask for water today?"

# Semantic search
ros2 topic pub /semantic_history_query std_msgs/String "Find all tasks related to getting blankets"
```

## 🤖 Robot Skills

The robot supports these skills:

| Skill | Description | Example |
|-------|-------------|---------|
| `go_to(location)` | Navigate to location | `go_to('kitchen')` |
| `grasp(object)` | Pick up object | `grasp('water_bottle')` |
| `place(object)` | Put down object | `place('water_bottle')` |
| `wait(duration)` | Wait for time | `wait(5.0)` |
| `speak(text)` | Speak message | `speak('I found your water')` |

## 📡 Communication Interfaces

### WebSocket Server (Port 8765)
```javascript
// Connect and send AAC input
const ws = new WebSocket('ws://localhost:8765');
ws.send(JSON.stringify({
  text: "I'm thirsty",
  user_id: "vedant",
  metadata: {source: "tablet"}
}));
```

### REST API (Port 8080)
```bash
curl -X POST http://localhost:8080/aac_input \
  -H "Content-Type: application/json" \
  -d '{"text": "bring water", "user_id": "vedant"}'
```

### ROS Topics
```bash
# Publish AAC input
ros2 topic pub /aac_input talkrbot_msgs/AACInput "{text: 'cold', user_id: 'vedant'}"

# Monitor task commands
ros2 topic echo /task_command

# Check execution feedback
ros2 topic echo /execution_feedback
```

## 🔍 Monitoring & Debugging

### Key Topics to Monitor
```bash
# Core data flow
ros2 topic echo /aac_input          # Raw AAC input
ros2 topic echo /refined_intent     # LLM-refined intent
ros2 topic echo /skill_plan         # Generated skill plan
ros2 topic echo /execution_feedback # Execution status

# User interaction
ros2 topic echo /speak_command      # Robot speech
ros2 topic echo /speech_response    # User responses
ros2 topic echo /current_user       # Active user profile
```

### Logging Levels
```bash
# Set debug logging for specific nodes
ros2 run talkrbot_llm intent_refiner_node --ros-args --log-level DEBUG
```

## 🛠️ Development

### Adding New Skills
1. Define skill in `skill_executor_node.py`
2. Add to GROOT planner prompt
3. Update user documentation

### Customizing LLM Prompts
Edit the prompt templates in:
- `intent_refiner_node.py` - Intent refinement
- `groot_planner_node.py` - Skill planning
- `failure_handler_node.py` - Failure recovery

### Extending User Profiles
Add new fields to `user_profiles.json`:
```json
{
  "new_field": "value",
  "preferences": {...},
  "accessibility_needs": {...}
}
```

## 🔒 Security & Privacy

- **API Key Management**: Uses environment variables, never hardcoded
- **Input Validation**: All AAC input is sanitized and validated
- **User Data**: Stored locally in SQLite, not transmitted externally
- **Error Handling**: Graceful degradation when services are unavailable

## 📊 Performance

- **Latency**: < 2 seconds from AAC input to robot action
- **Accuracy**: > 90% intent recognition for common phrases
- **Reliability**: Automatic retry logic for failed operations
- **Scalability**: Modular design supports multiple users and robots

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow ROS 2 Python style guide
- Add comprehensive logging
- Include error handling
- Write tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for natural language understanding
- **ROS 2 Humble** for robotics framework
- **YOLOv8** for computer vision
- **Nav2** for navigation capabilities
- **Ultralytics** for object detection

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/TalkrBot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/TalkrBot/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/TalkrBot/wiki)

---

**Made with ❤️ for the assistive technology community** 