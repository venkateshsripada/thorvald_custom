#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist



def main():
	rospy.init_node('command_velo', anonymous = True)
	pub = rospy.Publisher('/twist_mux/cmd_vel', Twist, queue_size = 10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		motion = Twist()
		motion.linear.x = 2.0
		motion.linear.y = 0.0
		motion.linear.z = 0.0

		motion.angular.x = 0.0
		motion.angular.y = 0.0
		motion.angular.z = 0.0
		pub.publish(motion)
		rate.sleep()


if __name__ == '__main__':
	
	main()
	
