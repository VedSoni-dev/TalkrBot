// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from talkrbot_msgs:msg/RefinedIntent.idl
// generated code does not contain a copyright notice
#include "talkrbot_msgs/msg/detail/refined_intent__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "talkrbot_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "talkrbot_msgs/msg/detail/refined_intent__struct.h"
#include "talkrbot_msgs/msg/detail/refined_intent__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "builtin_interfaces/msg/detail/time__functions.h"  // timestamp
#include "rosidl_runtime_c/string.h"  // intent, original_text, priority, user_location
#include "rosidl_runtime_c/string_functions.h"  // intent, original_text, priority, user_location

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_talkrbot_msgs
size_t get_serialized_size_builtin_interfaces__msg__Time(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_talkrbot_msgs
size_t max_serialized_size_builtin_interfaces__msg__Time(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_talkrbot_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, builtin_interfaces, msg, Time)();


using _RefinedIntent__ros_msg_type = talkrbot_msgs__msg__RefinedIntent;

static bool _RefinedIntent__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RefinedIntent__ros_msg_type * ros_message = static_cast<const _RefinedIntent__ros_msg_type *>(untyped_ros_message);
  // Field name: intent
  {
    const rosidl_runtime_c__String * str = &ros_message->intent;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: user_location
  {
    const rosidl_runtime_c__String * str = &ros_message->user_location;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: priority
  {
    const rosidl_runtime_c__String * str = &ros_message->priority;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: original_text
  {
    const rosidl_runtime_c__String * str = &ros_message->original_text;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: timestamp
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, builtin_interfaces, msg, Time
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->timestamp, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _RefinedIntent__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RefinedIntent__ros_msg_type * ros_message = static_cast<_RefinedIntent__ros_msg_type *>(untyped_ros_message);
  // Field name: intent
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->intent.data) {
      rosidl_runtime_c__String__init(&ros_message->intent);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->intent,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'intent'\n");
      return false;
    }
  }

  // Field name: user_location
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->user_location.data) {
      rosidl_runtime_c__String__init(&ros_message->user_location);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->user_location,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'user_location'\n");
      return false;
    }
  }

  // Field name: priority
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->priority.data) {
      rosidl_runtime_c__String__init(&ros_message->priority);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->priority,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'priority'\n");
      return false;
    }
  }

  // Field name: original_text
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->original_text.data) {
      rosidl_runtime_c__String__init(&ros_message->original_text);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->original_text,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'original_text'\n");
      return false;
    }
  }

  // Field name: timestamp
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, builtin_interfaces, msg, Time
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->timestamp))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_talkrbot_msgs
size_t get_serialized_size_talkrbot_msgs__msg__RefinedIntent(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RefinedIntent__ros_msg_type * ros_message = static_cast<const _RefinedIntent__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name intent
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->intent.size + 1);
  // field.name user_location
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->user_location.size + 1);
  // field.name priority
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->priority.size + 1);
  // field.name original_text
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->original_text.size + 1);
  // field.name timestamp

  current_alignment += get_serialized_size_builtin_interfaces__msg__Time(
    &(ros_message->timestamp), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _RefinedIntent__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_talkrbot_msgs__msg__RefinedIntent(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_talkrbot_msgs
size_t max_serialized_size_talkrbot_msgs__msg__RefinedIntent(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: intent
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: user_location
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: priority
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: original_text
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: timestamp
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_builtin_interfaces__msg__Time(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = talkrbot_msgs__msg__RefinedIntent;
    is_plain =
      (
      offsetof(DataType, timestamp) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RefinedIntent__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_talkrbot_msgs__msg__RefinedIntent(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RefinedIntent = {
  "talkrbot_msgs::msg",
  "RefinedIntent",
  _RefinedIntent__cdr_serialize,
  _RefinedIntent__cdr_deserialize,
  _RefinedIntent__get_serialized_size,
  _RefinedIntent__max_serialized_size
};

static rosidl_message_type_support_t _RefinedIntent__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RefinedIntent,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, talkrbot_msgs, msg, RefinedIntent)() {
  return &_RefinedIntent__type_support;
}

#if defined(__cplusplus)
}
#endif
