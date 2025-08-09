#include <rclcpp/rclcpp.hpp>
#include <behaviortree_cpp_v3/bt_factory.h>
#include <behaviortree_cpp_v3/loggers/bt_zmq_publisher.h>
#include <chrono>
#include <memory>
#include <string>

using namespace std::chrono_literals;

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("bt_executor_cpp");

  // Parameter for XML path
  std::string default_xml = std::string(
    std::getenv("HOME")) + "/TalkrBot/talkrbot_bt/bring_object.xml";
  std::string bt_xml_path = node->declare_parameter<std::string>("bt_xml_path", default_xml);

  RCLCPP_INFO(node->get_logger(), "Loading BT XML: %s", bt_xml_path.c_str());

  BT::BehaviorTreeFactory factory;
  // Register built-in nodes only. Custom ROS actions would be registered here.

  // Load tree from file
  BT::Tree tree = factory.createTreeFromFile(bt_xml_path);

  // ZMQ publisher for Groot (status on 1666, debug on 1667)
  BT::PublisherZMQ publisher_zmq(tree, 1666, 1667);

  // Tick until completion
  BT::NodeStatus status = BT::NodeStatus::RUNNING;
  while (rclcpp::ok() && status == BT::NodeStatus::RUNNING)
  {
    status = tree.tickRoot();
    rclcpp::spin_some(node);
    std::this_thread::sleep_for(50ms);
  }

  RCLCPP_INFO(node->get_logger(), "BT finished with status: %s",
              BT::toStr(status, true).c_str());

  rclcpp::shutdown();
  return 0;
} 