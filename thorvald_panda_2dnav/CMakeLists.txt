cmake_minimum_required(VERSION 3.0.2)
project(thorvald_2dnav)

find_package(catkin REQUIRED COMPONENTS
  move_base
  tf2
  tf2_ros
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)
