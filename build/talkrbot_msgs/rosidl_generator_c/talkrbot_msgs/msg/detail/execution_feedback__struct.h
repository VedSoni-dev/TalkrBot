// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_H_
#define TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'step'
// Member 'status'
// Member 'notes'
#include "rosidl_runtime_c/string.h"
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/ExecutionFeedback in the package talkrbot_msgs.
typedef struct talkrbot_msgs__msg__ExecutionFeedback
{
  /// e.g., "go_to('closet')"
  rosidl_runtime_c__String step;
  /// "success", "failure"
  rosidl_runtime_c__String status;
  /// Optional error notes or result
  rosidl_runtime_c__String notes;
  builtin_interfaces__msg__Time timestamp;
} talkrbot_msgs__msg__ExecutionFeedback;

// Struct for a sequence of talkrbot_msgs__msg__ExecutionFeedback.
typedef struct talkrbot_msgs__msg__ExecutionFeedback__Sequence
{
  talkrbot_msgs__msg__ExecutionFeedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} talkrbot_msgs__msg__ExecutionFeedback__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_H_
