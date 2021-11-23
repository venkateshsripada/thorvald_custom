cmake_minimum_required(VERSION 3.0.2)
project(thorvald_panda_description)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  controller_manager
  joint_state_controller
  robot_state_publisher
  gazebo_ros
)


catkin_package(
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
