// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__BUILDER_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "talkrbot_msgs/msg/detail/execution_feedback__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace talkrbot_msgs
{

namespace msg
{

namespace builder
{

class Init_ExecutionFeedback_timestamp
{
public:
  explicit Init_ExecutionFeedback_timestamp(::talkrbot_msgs::msg::ExecutionFeedback & msg)
  : msg_(msg)
  {}
  ::talkrbot_msgs::msg::ExecutionFeedback timestamp(::talkrbot_msgs::msg::ExecutionFeedback::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::talkrbot_msgs::msg::ExecutionFeedback msg_;
};

class Init_ExecutionFeedback_notes
{
public:
  explicit Init_ExecutionFeedback_notes(::talkrbot_msgs::msg::ExecutionFeedback & msg)
  : msg_(msg)
  {}
  Init_ExecutionFeedback_timestamp notes(::talkrbot_msgs::msg::ExecutionFeedback::_notes_type arg)
  {
    msg_.notes = std::move(arg);
    return Init_ExecutionFeedback_timestamp(msg_);
  }

private:
  ::talkrbot_msgs::msg::ExecutionFeedback msg_;
};

class Init_ExecutionFeedback_status
{
public:
  explicit Init_ExecutionFeedback_status(::talkrbot_msgs::msg::ExecutionFeedback & msg)
  : msg_(msg)
  {}
  Init_ExecutionFeedback_notes status(::talkrbot_msgs::msg::ExecutionFeedback::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_ExecutionFeedback_notes(msg_);
  }

private:
  ::talkrbot_msgs::msg::ExecutionFeedback msg_;
};

class Init_ExecutionFeedback_step
{
public:
  Init_ExecutionFeedback_step()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ExecutionFeedback_status step(::talkrbot_msgs::msg::ExecutionFeedback::_step_type arg)
  {
    msg_.step = std::move(arg);
    return Init_ExecutionFeedback_status(msg_);
  }

private:
  ::talkrbot_msgs::msg::ExecutionFeedback msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::talkrbot_msgs::msg::ExecutionFeedback>()
{
  return talkrbot_msgs::msg::builder::Init_ExecutionFeedback_step();
}

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__BUILDER_HPP_
