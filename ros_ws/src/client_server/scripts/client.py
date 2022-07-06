#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolRequest

#initialize node
rospy.init_node("client_node")

#create client
client = rospy.ServiceProxy("/bool_service",SetBool)

#wait for server to init
rospy.wait_for_service("/bool_service")

while not rospy.is_shutdown():
    #create request
    request = SetBoolRequest()
    request.data = True

    #send request and wait for response
    response = client(request)
    print(response)
    rospy.sleep(1)