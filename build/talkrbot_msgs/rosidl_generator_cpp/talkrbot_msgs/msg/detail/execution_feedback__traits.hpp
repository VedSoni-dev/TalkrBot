// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__TRAITS_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "talkrbot_msgs/msg/detail/execution_feedback__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace talkrbot_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ExecutionFeedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: step
  {
    out << "step: ";
    rosidl_generator_traits::value_to_yaml(msg.step, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: notes
  {
    out << "notes: ";
    rosidl_generator_traits::value_to_yaml(msg.notes, out);
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
  const ExecutionFeedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: step
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "step: ";
    rosidl_generator_traits::value_to_yaml(msg.step, out);
    out << "\n";
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: notes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "notes: ";
    rosidl_generator_traits::value_to_yaml(msg.notes, out);
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

inline std::string to_yaml(const ExecutionFeedback & msg, bool use_flow_style = false)
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
  const talkrbot_msgs::msg::ExecutionFeedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  talkrbot_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use talkrbot_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const talkrbot_msgs::msg::ExecutionFeedback & msg)
{
  return talkrbot_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<talkrbot_msgs::msg::ExecutionFeedback>()
{
  return "talkrbot_msgs::msg::ExecutionFeedback";
}

template<>
inline const char * name<talkrbot_msgs::msg::ExecutionFeedback>()
{
  return "talkrbot_msgs/msg/ExecutionFeedback";
}

template<>
struct has_fixed_size<talkrbot_msgs::msg::ExecutionFeedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<talkrbot_msgs::msg::ExecutionFeedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<talkrbot_msgs::msg::ExecutionFeedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__TRAITS_HPP_
