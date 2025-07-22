// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__TRAITS_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "talkrbot_msgs/msg/detail/task_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace talkrbot_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TaskCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: task
  {
    out << "task: ";
    rosidl_generator_traits::value_to_yaml(msg.task, out);
    out << ", ";
  }

  // member: object
  {
    out << "object: ";
    rosidl_generator_traits::value_to_yaml(msg.object, out);
    out << ", ";
  }

  // member: location
  {
    out << "location: ";
    rosidl_generator_traits::value_to_yaml(msg.location, out);
    out << ", ";
  }

  // member: parameters
  {
    out << "parameters: ";
    rosidl_generator_traits::value_to_yaml(msg.parameters, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: command_id
  {
    out << "command_id: ";
    rosidl_generator_traits::value_to_yaml(msg.command_id, out);
    out << ", ";
  }

  // member: timestamp
  {
    out << "timestamp: ";
    to_flow_style_yaml(msg.timestamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: task
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task: ";
    rosidl_generator_traits::value_to_yaml(msg.task, out);
    out << "\n";
  }

  // member: object
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "object: ";
    rosidl_generator_traits::value_to_yaml(msg.object, out);
    out << "\n";
  }

  // member: location
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "location: ";
    rosidl_generator_traits::value_to_yaml(msg.location, out);
    out << "\n";
  }

  // member: parameters
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "parameters: ";
    rosidl_generator_traits::value_to_yaml(msg.parameters, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }

  // member: command_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command_id: ";
    rosidl_generator_traits::value_to_yaml(msg.command_id, out);
    out << "\n";
  }

  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp:\n";
    to_block_style_yaml(msg.timestamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskCommand & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace talkrbot_msgs

namespace rosidl_generator_traits
{

[[deprecated("use talkrbot_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const talkrbot_msgs::msg::TaskCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  talkrbot_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use talkrbot_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const talkrbot_msgs::msg::TaskCommand & msg)
{
  return talkrbot_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<talkrbot_msgs::msg::TaskCommand>()
{
  return "talkrbot_msgs::msg::TaskCommand";
}

template<>
inline const char * name<talkrbot_msgs::msg::TaskCommand>()
{
  return "talkrbot_msgs/msg/TaskCommand";
}

template<>
struct has_fixed_size<talkrbot_msgs::msg::TaskCommand>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<talkrbot_msgs::msg::TaskCommand>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<talkrbot_msgs::msg::TaskCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__TRAITS_HPP_
