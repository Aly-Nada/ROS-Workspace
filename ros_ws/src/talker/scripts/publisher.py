#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

#Initialize ros node

rospy.init_node("Publisher_Node")
publisher = rospy.Publisher("/phrase", String, queue_size = 10)

while not rospy.is_shutdown():
	#creating msg
	message = String()
	message.data = rospy.get_param("phrase")
	
	publisher.publish(message)
	rospy.sleep(1)
