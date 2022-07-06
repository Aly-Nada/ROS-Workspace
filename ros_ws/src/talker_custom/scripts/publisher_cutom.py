#!/usr/bin/env python3

import rospy
from talker_custom.msg import custom_message

rospy.init_node("Publisher_custom")

publisher = rospy.Publisher("/custom_topic", custom_message, queue_size=10)

while not rospy.is_shutdown:
    msg = custom_message()
    msg.number = 25
    msg.flag = False
    msg.phrase = "yes"


    publisher.publish(msg)
    rospy.sleep(1)