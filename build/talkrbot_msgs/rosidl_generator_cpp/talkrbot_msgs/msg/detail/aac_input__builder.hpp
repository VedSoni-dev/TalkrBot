// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__BUILDER_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "talkrbot_msgs/msg/detail/aac_input__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace talkrbot_msgs
{

namespace msg
{

namespace builder
{

class Init_AACInput_metadata
{
public:
  explicit Init_AACInput_metadata(::talkrbot_msgs::msg::AACInput & msg)
  : msg_(msg)
  {}
  ::talkrbot_msgs::msg::AACInput metadata(::talkrbot_msgs::msg::AACInput::_metadata_type arg)
  {
    msg_.metadata = std::move(arg);
    return std::move(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

class Init_AACInput_confidence
{
public:
  explicit Init_AACInput_confidence(::talkrbot_msgs::msg::AACInput & msg)
  : msg_(msg)
  {}
  Init_AACInput_metadata confidence(::talkrbot_msgs::msg::AACInput::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_AACInput_metadata(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

class Init_AACInput_input_method
{
public:
  explicit Init_AACInput_input_method(::talkrbot_msgs::msg::AACInput & msg)
  : msg_(msg)
  {}
  Init_AACInput_confidence input_method(::talkrbot_msgs::msg::AACInput::_input_method_type arg)
  {
    msg_.input_method = std::move(arg);
    return Init_AACInput_confidence(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

class Init_AACInput_timestamp
{
public:
  explicit Init_AACInput_timestamp(::talkrbot_msgs::msg::AACInput & msg)
  : msg_(msg)
  {}
  Init_AACInput_input_method timestamp(::talkrbot_msgs::msg::AACInput::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_AACInput_input_method(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

class Init_AACInput_user_id
{
public:
  explicit Init_AACInput_user_id(::talkrbot_msgs::msg::AACInput & msg)
  : msg_(msg)
  {}
  Init_AACInput_timestamp user_id(::talkrbot_msgs::msg::AACInput::_user_id_type arg)
  {
    msg_.user_id = std::move(arg);
    return Init_AACInput_timestamp(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

class Init_AACInput_text
{
public:
  Init_AACInput_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AACInput_user_id text(::talkrbot_msgs::msg::AACInput::_text_type arg)
  {
    msg_.text = std::move(arg);
    return Init_AACInput_user_id(msg_);
  }

private:
  ::talkrbot_msgs::msg::AACInput msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::talkrbot_msgs::msg::AACInput>()
{
  return talkrbot_msgs::msg::builder::Init_AACInput_text();
}

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__BUILDER_HPP_
