// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "talkrbot_msgs/msg/detail/execution_feedback__rosidl_typesupport_introspection_c.h"
#include "talkrbot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "talkrbot_msgs/msg/detail/execution_feedback__functions.h"
#include "talkrbot_msgs/msg/detail/execution_feedback__struct.h"


// Include directives for member types
// Member `step`
// Member `status`
// Member `notes`
#include "rosidl_runtime_c/string_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/time.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  talkrbot_msgs__msg__ExecutionFeedback__init(message_memory);
}

void talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_fini_function(void * message_memory)
{
  talkrbot_msgs__msg__ExecutionFeedback__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_member_array[4] = {
  {
    "step",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(talkrbot_msgs__msg__ExecutionFeedback, step),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(talkrbot_msgs__msg__ExecutionFeedback, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "notes",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(talkrbot_msgs__msg__ExecutionFeedback, notes),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(talkrbot_msgs__msg__ExecutionFeedback, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_members = {
  "talkrbot_msgs__msg",  // message namespace
  "ExecutionFeedback",  // message name
  4,  // number of fields
  sizeof(talkrbot_msgs__msg__ExecutionFeedback),
  talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_member_array,  // message members
  talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_init_function,  // function to initialize message memory (memory has to be allocated)
  talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_type_support_handle = {
  0,
  &talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_talkrbot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, talkrbot_msgs, msg, ExecutionFeedback)() {
  talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_type_support_handle.typesupport_identifier) {
    talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &talkrbot_msgs__msg__ExecutionFeedback__rosidl_typesupport_introspection_c__ExecutionFeedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
