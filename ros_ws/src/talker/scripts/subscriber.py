#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_fn(p):
	print("Received Messag = ", p.data)


#initialize
rospy.init_node("Subscriber_Node")

rospy.Subscriber("/phrase", String, callback_fn)
rospy.spin()
