string text                     # Raw text input from AAC device
string user_id                  # User identifier for personalization
builtin_interfaces/Time timestamp  # Timestamp of input
string input_method             # Source of input (websocket, http, ros_topic, etc.)
float32 confidence              # Confidence score (0.0 to 1.0)
string metadata                 # Additional metadata as JSON string 