cmake_minimum_required(VERSION 3.0.2)
project(realsense_t265)

find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)