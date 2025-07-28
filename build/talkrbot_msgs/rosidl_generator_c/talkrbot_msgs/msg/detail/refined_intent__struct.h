// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from talkrbot_msgs:msg/RefinedIntent.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_H_
#define TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'intent'
// Member 'user_location'
// Member 'priority'
// Member 'original_text'
#include "rosidl_runtime_c/string.h"
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/RefinedIntent in the package talkrbot_msgs.
typedef struct talkrbot_msgs__msg__RefinedIntent
{
  /// The final interpreted task (e.g. "bring blanket")
  rosidl_runtime_c__String intent;
  /// Optional, like "couch" or "living room"
  rosidl_runtime_c__String user_location;
  /// e.g., "high", "normal"
  rosidl_runtime_c__String priority;
  /// The raw AAC input text
  rosidl_runtime_c__String original_text;
  builtin_interfaces__msg__Time timestamp;
} talkrbot_msgs__msg__RefinedIntent;

// Struct for a sequence of talkrbot_msgs__msg__RefinedIntent.
typedef struct talkrbot_msgs__msg__RefinedIntent__Sequence
{
  talkrbot_msgs__msg__RefinedIntent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} talkrbot_msgs__msg__RefinedIntent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_H_
