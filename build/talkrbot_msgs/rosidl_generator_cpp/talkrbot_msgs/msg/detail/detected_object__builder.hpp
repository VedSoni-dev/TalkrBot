// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from talkrbot_msgs:msg/DetectedObject.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__BUILDER_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "talkrbot_msgs/msg/detail/detected_object__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace talkrbot_msgs
{

namespace msg
{

namespace builder
{

class Init_DetectedObject_timestamp
{
public:
  explicit Init_DetectedObject_timestamp(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  ::talkrbot_msgs::msg::DetectedObject timestamp(::talkrbot_msgs::msg::DetectedObject::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_object_id
{
public:
  explicit Init_DetectedObject_object_id(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_timestamp object_id(::talkrbot_msgs::msg::DetectedObject::_object_id_type arg)
  {
    msg_.object_id = std::move(arg);
    return Init_DetectedObject_timestamp(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_properties
{
public:
  explicit Init_DetectedObject_properties(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_object_id properties(::talkrbot_msgs::msg::DetectedObject::_properties_type arg)
  {
    msg_.properties = std::move(arg);
    return Init_DetectedObject_object_id(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_pose
{
public:
  explicit Init_DetectedObject_pose(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_properties pose(::talkrbot_msgs::msg::DetectedObject::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_DetectedObject_properties(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_bbox_height
{
public:
  explicit Init_DetectedObject_bbox_height(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_pose bbox_height(::talkrbot_msgs::msg::DetectedObject::_bbox_height_type arg)
  {
    msg_.bbox_height = std::move(arg);
    return Init_DetectedObject_pose(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_bbox_width
{
public:
  explicit Init_DetectedObject_bbox_width(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_bbox_height bbox_width(::talkrbot_msgs::msg::DetectedObject::_bbox_width_type arg)
  {
    msg_.bbox_width = std::move(arg);
    return Init_DetectedObject_bbox_height(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_bbox_y
{
public:
  explicit Init_DetectedObject_bbox_y(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_bbox_width bbox_y(::talkrbot_msgs::msg::DetectedObject::_bbox_y_type arg)
  {
    msg_.bbox_y = std::move(arg);
    return Init_DetectedObject_bbox_width(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_bbox_x
{
public:
  explicit Init_DetectedObject_bbox_x(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_bbox_y bbox_x(::talkrbot_msgs::msg::DetectedObject::_bbox_x_type arg)
  {
    msg_.bbox_x = std::move(arg);
    return Init_DetectedObject_bbox_y(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_confidence
{
public:
  explicit Init_DetectedObject_confidence(::talkrbot_msgs::msg::DetectedObject & msg)
  : msg_(msg)
  {}
  Init_DetectedObject_bbox_x confidence(::talkrbot_msgs::msg::DetectedObject::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_DetectedObject_bbox_x(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

class Init_DetectedObject_class_name
{
public:
  Init_DetectedObject_class_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectedObject_confidence class_name(::talkrbot_msgs::msg::DetectedObject::_class_name_type arg)
  {
    msg_.class_name = std::move(arg);
    return Init_DetectedObject_confidence(msg_);
  }

private:
  ::talkrbot_msgs::msg::DetectedObject msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::talkrbot_msgs::msg::DetectedObject>()
{
  return talkrbot_msgs::msg::builder::Init_DetectedObject_class_name();
}

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__DETECTED_OBJECT__BUILDER_HPP_
