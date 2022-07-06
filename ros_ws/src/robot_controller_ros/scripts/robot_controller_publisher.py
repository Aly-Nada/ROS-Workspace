#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose

def publisher():

	pub = rospy.Publisher('pose', Pose, queue_size=10)
	rospy.init_node('position_publisher', anonymous=True)
	rate = rospy.Rate(1) # 10hz

	while not rospy.is_shutdown():
		
		pos=Pose()
		pos.position.x=rospy.get_param("x")
		pos.position.y=rospy.get_param("y")
		pos.position.z=rospy.get_param("z")
		pos.orientation.w=rospy.get_param("rot_w")
		pos.orientation.x=rospy.get_param("rot_x")
		pos.orientation.y=rospy.get_param("rot_y")
		pos.orientation.z=rospy.get_param("rot_z")
			
		pub.publish(pos)   
		rospy.loginfo(pos) 
		rate.sleep() 

if __name__ =='__main__':
	try:
		publisher()

	except rospy.ROSInterruptException:
		pass