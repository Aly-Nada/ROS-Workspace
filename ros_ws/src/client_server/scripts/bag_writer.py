#!/usr/bin/env python3

import rospy
import rosbag

from std_msgs.msg import String, Int32

#initialize node
rospy.init_node("bag_reader")

#Create a new bag file or edit on existing one
bag_obj = rosbag.Bag("/home/alynada/ros_ws/src/client_server/bags/test.bag",'w')

msg_string = String()
msg_string.data = 'message 1'

msg_int = Int32()
msg_int.data = 25

bag_obj.write('/topic1',msg_string)
bag_obj.write('/topic2',msg_int)

bag_obj.close()