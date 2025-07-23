// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from talkrbot_msgs:msg/DetectedObject.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__STRUCT_H_
#define TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'class_name'
// Member 'properties'
// Member 'object_id'
#include "rosidl_runtime_c/string.h"
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.h"
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/DetectedObject in the package talkrbot_msgs.
typedef struct talkrbot_msgs__msg__DetectedObject
{
  /// e.g., "water bottle"
  rosidl_runtime_c__String class_name;
  /// Detection confidence (0.0–1.0)
  float confidence;
  int32_t bbox_x;
  int32_t bbox_y;
  int32_t bbox_width;
  int32_t bbox_height;
  /// 3D position in world coordinates
  geometry_msgs__msg__PoseStamped pose;
  /// JSON string with additional properties
  rosidl_runtime_c__String properties;
  /// Unique object ID
  rosidl_runtime_c__String object_id;
  builtin_interfaces__msg__Time timestamp;
} talkrbot_msgs__msg__DetectedObject;

// Struct for a sequence of talkrbot_msgs__msg__DetectedObject.
typedef struct talkrbot_msgs__msg__DetectedObject__Sequence
{
  talkrbot_msgs__msg__DetectedObject * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} talkrbot_msgs__msg__DetectedObject__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__STRUCT_H_
