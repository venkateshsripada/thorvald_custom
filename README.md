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


### List of todos: 

1) Add franka panda in urdf and separate all the transmission, gazebo plugins, joints/links in separate file so that it is properly. maintained.
2) Add franka simulation (controller and gazebo simulation, moveit etc.). 
3) Add navigation stack fully and test with automatic navigation 
4) Integrate thorvald real cotnroller nodes.
5) Package testing and cleaning. 
6) Move all the thorvald-* package dependencies to this package (probably in the a separate third_party folder so that this package is self-contained without any broken dependencies).
7) Release different version for kinetic and melodic (LEAST PRIORITY) 
