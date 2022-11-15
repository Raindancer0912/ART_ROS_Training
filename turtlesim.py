import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import math

class Location:
    def __init__(self):
        self.x=pose.Point.x
        self.y=pose.Point.y
        self.y=pose.Point.z

def move_to_goal(x_goal,y_goal):
    rospy.init_node("move_to_goal",anonymous=True)

    x=Location.x
    y=Location.y

    velocity=Twist()
    check_status=True
    tolerance=
    while check_status:
        distance = sqrt((x_goal-x)**2+(y_goal-y)**2)
        if distance < tolerance:
            check_status=False
            velocity_linear=0
            velocity_angular=0
        else:
            velocity.linear.x=1.0
            velocity.linear.y=0
            velocity.linear.z=0
            velocity.angular=arctan((y_goal-y)/(x_goal-x))

def callback(pose):
    rospy.loginfo(rospy_get_caller_id()+"I heard %s", data.data)

if __name__=="__main__":
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    rospy.Publish("/turtle1/cmd_vel",Point,queue_size=10)
    move_to_goal()


#velocity (twist) is a vector so each of its parameters needs to be defined
#put subscriber and publisher in the main function --> main function only gets called once, and therefore only one subscribe
#is generated. if put in function, new one created each time function is called -->not ideal
#define a class/global variable such that a location (point(x,y,z)) can be accesssed across the script