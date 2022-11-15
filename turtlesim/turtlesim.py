import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
import math

def move_to_goal(x_goal,y_goal):
    pub = rospy.Publisher("/turtle1/cmd_vel",Float64,queue_size=10)
    rospy.init_node("move_to_goal",anonymous=True)

    x=Point.x()
    y=Point.y()

    velocity=Twist()
    check_status=True
    while check_status:
        distance = sqrt((x_goal-x)**2+(y_goal-y)**2)
        if distance < 0.1:
            check_status=False
            velocity_linear=0
            velocity_angular=0
        else:
            velocity.linear=1.0
            volocity.angular=arctan((y_goal-y)/(x_goal-x))
        






    


