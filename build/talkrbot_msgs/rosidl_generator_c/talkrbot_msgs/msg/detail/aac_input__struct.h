// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_H_
#define TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'text'
// Member 'user_id'
// Member 'input_method'
// Member 'metadata'
#include "rosidl_runtime_c/string.h"
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/AACInput in the package talkrbot_msgs.
typedef struct talkrbot_msgs__msg__AACInput
{
  /// Raw text input from AAC device
  rosidl_runtime_c__String text;
  /// User identifier for personalization
  rosidl_runtime_c__String user_id;
  /// Timestamp of input
  builtin_interfaces__msg__Time timestamp;
  /// Source of input (websocket, http, ros_topic, etc.)
  rosidl_runtime_c__String input_method;
  /// Confidence score (0.0 to 1.0)
  float confidence;
  /// Additional metadata as JSON string
  rosidl_runtime_c__String metadata;
} talkrbot_msgs__msg__AACInput;

// Struct for a sequence of talkrbot_msgs__msg__AACInput.
typedef struct talkrbot_msgs__msg__AACInput__Sequence
{
  talkrbot_msgs__msg__AACInput * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} talkrbot_msgs__msg__AACInput__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_H_
