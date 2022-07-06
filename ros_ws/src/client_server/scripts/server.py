#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest

def server_cb(req):
    
    response = SetBoolResponse()
    if req.data == True:
        response.success = True
        response.message = "Received True variable"
    else:
        response.success = False
        response.message = "Received False message"
    return response

rospy.init_node("server_node")
rospy.Service("/bool_service", SetBool, server_cb)


rospy.spin()