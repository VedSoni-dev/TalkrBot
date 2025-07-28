// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from talkrbot_msgs:msg/RefinedIntent.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__TRAITS_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "talkrbot_msgs/msg/detail/refined_intent__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace talkrbot_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RefinedIntent & msg,
  std::ostream & out)
{
  out << "{";
  // member: intent
  {
    out << "intent: ";
    rosidl_generator_traits::value_to_yaml(msg.intent, out);
    out << ", ";
  }

  // member: user_location
  {
    out << "user_location: ";
    rosidl_generator_traits::value_to_yaml(msg.user_location, out);
    out << ", ";
  }

  // member: priority
  {
    out << "priority: ";
    rosidl_generator_traits::value_to_yaml(msg.priority, out);
    out << ", ";
  }

  // member: original_text
  {
    out << "original_text: ";
    rosidl_generator_traits::value_to_yaml(msg.original_text, out);
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
  const RefinedIntent & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: intent
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "intent: ";
    rosidl_generator_traits::value_to_yaml(msg.intent, out);
    out << "\n";
  }

  // member: user_location
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "user_location: ";
    rosidl_generator_traits::value_to_yaml(msg.user_location, out);
    out << "\n";
  }

  // member: priority
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "priority: ";
    rosidl_generator_traits::value_to_yaml(msg.priority, out);
    out << "\n";
  }

  // member: original_text
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "original_text: ";
    rosidl_generator_traits::value_to_yaml(msg.original_text, out);
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

inline std::string to_yaml(const RefinedIntent & msg, bool use_flow_style = false)
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
  const talkrbot_msgs::msg::RefinedIntent & msg,
  std::ostream & out, size_t indentation = 0)
{
  talkrbot_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use talkrbot_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const talkrbot_msgs::msg::RefinedIntent & msg)
{
  return talkrbot_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<talkrbot_msgs::msg::RefinedIntent>()
{
  return "talkrbot_msgs::msg::RefinedIntent";
}

template<>
inline const char * name<talkrbot_msgs::msg::RefinedIntent>()
{
  return "talkrbot_msgs/msg/RefinedIntent";
}

template<>
struct has_fixed_size<talkrbot_msgs::msg::RefinedIntent>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<talkrbot_msgs::msg::RefinedIntent>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<talkrbot_msgs::msg::RefinedIntent>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__TRAITS_HPP_
