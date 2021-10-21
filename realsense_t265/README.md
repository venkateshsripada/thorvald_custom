# Realsense T625 - ROS/Gazebo simulation package

A model for the [Intel Realsense T625 Tracking Camera](https://www.intelrealsense.com/tracking-camera-t265/) to be used for simulation in ROS/Gazebo.

This package is based on [realsense_ros_gazebo by nilseuropa](https://github.com/nilseuropa/realsense_ros_gazebo).

## Usage

```xml
<xacro:include filename="$(find realsense_t265)/urdf/_t265.urdf.xacro"/>

<xacro:realsense_t265 robot_ns="" sensor_name="camera" parent_link="base_link" rate="30.0">
  <origin rpy="0 0 0" xyz="0 0 0.5"/>
</xacro:realsense_t265>
```

The package will publish messages on the following topics:

- `/camera/fisheye1/*`: left fisheye camera
- `/camera/fisheye2/*`: right fisheye camera
- `/camera/gyro/sample`: IMU with gyroscope and accelerometer
- `/camera/odom/sample`: odometry data
