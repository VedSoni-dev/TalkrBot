// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from talkrbot_msgs:msg/RefinedIntent.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__BUILDER_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "talkrbot_msgs/msg/detail/refined_intent__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace talkrbot_msgs
{

namespace msg
{

namespace builder
{

class Init_RefinedIntent_timestamp
{
public:
  explicit Init_RefinedIntent_timestamp(::talkrbot_msgs::msg::RefinedIntent & msg)
  : msg_(msg)
  {}
  ::talkrbot_msgs::msg::RefinedIntent timestamp(::talkrbot_msgs::msg::RefinedIntent::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::talkrbot_msgs::msg::RefinedIntent msg_;
};

class Init_RefinedIntent_original_text
{
public:
  explicit Init_RefinedIntent_original_text(::talkrbot_msgs::msg::RefinedIntent & msg)
  : msg_(msg)
  {}
  Init_RefinedIntent_timestamp original_text(::talkrbot_msgs::msg::RefinedIntent::_original_text_type arg)
  {
    msg_.original_text = std::move(arg);
    return Init_RefinedIntent_timestamp(msg_);
  }

private:
  ::talkrbot_msgs::msg::RefinedIntent msg_;
};

class Init_RefinedIntent_priority
{
public:
  explicit Init_RefinedIntent_priority(::talkrbot_msgs::msg::RefinedIntent & msg)
  : msg_(msg)
  {}
  Init_RefinedIntent_original_text priority(::talkrbot_msgs::msg::RefinedIntent::_priority_type arg)
  {
    msg_.priority = std::move(arg);
    return Init_RefinedIntent_original_text(msg_);
  }

private:
  ::talkrbot_msgs::msg::RefinedIntent msg_;
};

class Init_RefinedIntent_user_location
{
public:
  explicit Init_RefinedIntent_user_location(::talkrbot_msgs::msg::RefinedIntent & msg)
  : msg_(msg)
  {}
  Init_RefinedIntent_priority user_location(::talkrbot_msgs::msg::RefinedIntent::_user_location_type arg)
  {
    msg_.user_location = std::move(arg);
    return Init_RefinedIntent_priority(msg_);
  }

private:
  ::talkrbot_msgs::msg::RefinedIntent msg_;
};

class Init_RefinedIntent_intent
{
public:
  Init_RefinedIntent_intent()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RefinedIntent_user_location intent(::talkrbot_msgs::msg::RefinedIntent::_intent_type arg)
  {
    msg_.intent = std::move(arg);
    return Init_RefinedIntent_user_location(msg_);
  }

private:
  ::talkrbot_msgs::msg::RefinedIntent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::talkrbot_msgs::msg::RefinedIntent>()
{
  return talkrbot_msgs::msg::builder::Init_RefinedIntent_intent();
}

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__BUILDER_HPP_
