## Haptic Mobile Manipulation ROS Package: 

This package combines Thorvald robot (first gen) with franka panda through a custom fixture. 

The package will contain both the simulation and real robot control, description, trajectory controllers, moveit planing and navigation packages. 


### Install:

Install the Thorvald packages as follow: 

```bash
 $ sudo apt-get install ros-$ROS_DISTRO-thorvald-*
```

Create a catkin workspace and build the packges : 


```bash
$ cd 
$ mkdir -p ~/mobile_ws/src
$ cd mobile_ws/src 
$ git clone https://github.com/venkateshsripada/thorvald_custom.git
$ cd ..
$ catkin_make
```


Run the Gazebo simulation with simulated gazebo controllers as follow: 


```bash
$ cd 
$ cd mobile_ws
$ source devel/setup.bash
$ roslaunch thorvald_panda_description thorvald_panda_gazebo.launch
```