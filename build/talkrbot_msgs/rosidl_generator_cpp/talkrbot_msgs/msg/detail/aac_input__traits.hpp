// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__TRAITS_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "talkrbot_msgs/msg/detail/aac_input__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace talkrbot_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const AACInput & msg,
  std::ostream & out)
{
  out << "{";
  // member: text
  {
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
    out << ", ";
  }

  // member: user_id
  {
    out << "user_id: ";
    rosidl_generator_traits::value_to_yaml(msg.user_id, out);
    out << ", ";
  }

  // member: timestamp
  {
    out << "timestamp: ";
    to_flow_style_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: input_method
  {
    out << "input_method: ";
    rosidl_generator_traits::value_to_yaml(msg.input_method, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: metadata
  {
    out << "metadata: ";
    rosidl_generator_traits::value_to_yaml(msg.metadata, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AACInput & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: text
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
    out << "\n";
  }

  // member: user_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "user_id: ";
    rosidl_generator_traits::value_to_yaml(msg.user_id, out);
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

  // member: input_method
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "input_method: ";
    rosidl_generator_traits::value_to_yaml(msg.input_method, out);
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

  // member: metadata
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "metadata: ";
    rosidl_generator_traits::value_to_yaml(msg.metadata, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AACInput & msg, bool use_flow_style = false)
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
  const talkrbot_msgs::msg::AACInput & msg,
  std::ostream & out, size_t indentation = 0)
{
  talkrbot_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use talkrbot_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const talkrbot_msgs::msg::AACInput & msg)
{
  return talkrbot_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<talkrbot_msgs::msg::AACInput>()
{
  return "talkrbot_msgs::msg::AACInput";
}

template<>
inline const char * name<talkrbot_msgs::msg::AACInput>()
{
  return "talkrbot_msgs/msg/AACInput";
}

template<>
struct has_fixed_size<talkrbot_msgs::msg::AACInput>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<talkrbot_msgs::msg::AACInput>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<talkrbot_msgs::msg::AACInput>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__TRAITS_HPP_
