// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_H_
#define TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'task'
// Member 'object'
// Member 'location'
// Member 'parameters'
// Member 'command_id'
#include "rosidl_runtime_c/string.h"
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/TaskCommand in the package talkrbot_msgs.
typedef struct talkrbot_msgs__msg__TaskCommand
{
  rosidl_runtime_c__String task;
  rosidl_runtime_c__String object;
  rosidl_runtime_c__String location;
  rosidl_runtime_c__String parameters;
  float confidence;
  rosidl_runtime_c__String command_id;
  builtin_interfaces__msg__Time timestamp;
} talkrbot_msgs__msg__TaskCommand;

// Struct for a sequence of talkrbot_msgs__msg__TaskCommand.
typedef struct talkrbot_msgs__msg__TaskCommand__Sequence
{
  talkrbot_msgs__msg__TaskCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} talkrbot_msgs__msg__TaskCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_H_
