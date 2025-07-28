// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__BUILDER_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "talkrbot_msgs/msg/detail/task_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace talkrbot_msgs
{

namespace msg
{

namespace builder
{

class Init_TaskCommand_timestamp
{
public:
  explicit Init_TaskCommand_timestamp(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  ::talkrbot_msgs::msg::TaskCommand timestamp(::talkrbot_msgs::msg::TaskCommand::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_command_id
{
public:
  explicit Init_TaskCommand_command_id(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  Init_TaskCommand_timestamp command_id(::talkrbot_msgs::msg::TaskCommand::_command_id_type arg)
  {
    msg_.command_id = std::move(arg);
    return Init_TaskCommand_timestamp(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_confidence
{
public:
  explicit Init_TaskCommand_confidence(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  Init_TaskCommand_command_id confidence(::talkrbot_msgs::msg::TaskCommand::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_TaskCommand_command_id(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_parameters
{
public:
  explicit Init_TaskCommand_parameters(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  Init_TaskCommand_confidence parameters(::talkrbot_msgs::msg::TaskCommand::_parameters_type arg)
  {
    msg_.parameters = std::move(arg);
    return Init_TaskCommand_confidence(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_location
{
public:
  explicit Init_TaskCommand_location(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  Init_TaskCommand_parameters location(::talkrbot_msgs::msg::TaskCommand::_location_type arg)
  {
    msg_.location = std::move(arg);
    return Init_TaskCommand_parameters(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_object
{
public:
  explicit Init_TaskCommand_object(::talkrbot_msgs::msg::TaskCommand & msg)
  : msg_(msg)
  {}
  Init_TaskCommand_location object(::talkrbot_msgs::msg::TaskCommand::_object_type arg)
  {
    msg_.object = std::move(arg);
    return Init_TaskCommand_location(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

class Init_TaskCommand_task
{
public:
  Init_TaskCommand_task()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskCommand_object task(::talkrbot_msgs::msg::TaskCommand::_task_type arg)
  {
    msg_.task = std::move(arg);
    return Init_TaskCommand_object(msg_);
  }

private:
  ::talkrbot_msgs::msg::TaskCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::talkrbot_msgs::msg::TaskCommand>()
{
  return talkrbot_msgs::msg::builder::Init_TaskCommand_task();
}

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__BUILDER_HPP_
