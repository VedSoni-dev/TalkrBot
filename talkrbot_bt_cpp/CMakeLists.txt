cmake_minimum_required(VERSION 3.8)
project(talkrbot_bt_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(behaviortree_cpp_v3 REQUIRED)

add_executable(bt_executor src/bt_executor.cpp)
ament_target_dependencies(bt_executor rclcpp behaviortree_cpp_v3)

target_compile_features(bt_executor PUBLIC cxx_std_17)

target_link_libraries(bt_executor
  ${behaviortree_cpp_v3_LIBRARIES}
)

target_include_directories(bt_executor PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

install(TARGETS bt_executor
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY ${CMAKE_SOURCE_DIR}/../talkrbot_bt/
  DESTINATION share/${PROJECT_NAME}/bt
  FILES_MATCHING PATTERN "*.xml"
)

ament_package() 