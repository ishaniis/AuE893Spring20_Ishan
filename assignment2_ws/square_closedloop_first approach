#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg      import Pose
from math               import pow,atan2,sqrt

class TurtleBot():

    def __init__(self):
    #Initialising the node go2goal_turtle 
        rospy.init_node('go2goal_turtle', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber    = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
    #Callback function which is called when a new message of type Pose is received by the subscriber
        self.pose = data
        self.pose.x = round(self.pose.x, 8)
        self.pose.y = round(self.pose.y, 8)

    def euclidian_distance(self, goal_pose):
    #distance between goal and current pose
        distance = sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
        return distance

    #def linear_vel(self,goal_pose, constant =1):
	#return constant * self.euclidian_distance(goal_pose)

    #def steering_angle(self,goal_pose):
	#angle =atan2(goal_pose.y-self.pose.y,goal_pose.x-self.pose.x)
	#return angle

    #def angular_vel(self,goal_pose, constant=6):
	#return constant*(self.steering_angle(goal_pose) -self.pose.theta)

    def move2goal(self):
    #function to move the turtle towards the goal#
	coordinate = [[0,0], [0,0], [0,0], [0,0], [0,0]]
        goal_pose = Pose()

	for i in range(0,5):
        #user input
	    pose_x = input("Set your X coordinate: ")
	    pose_y = input("Set your Y coordinate: ")
	    coordinate[i][0] = pose_x
	    coordinate[i][1] = pose_y
	
        distance_tolerance = input("Set your tolerance slightly above 0:")
        vel_msg = Twist()

	for j in range(0,5):
      	
            while abs((atan2(coordinate[j][1] - self.pose.y, coordinate[j][0] - self.pose.x) - self.pose.theta)) >= 0.005:
            
            #Porportional Controller
	    #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 1.5 * (atan2(coordinate[j][1] - self.pose.y, coordinate[j][0] - self.pose.x) - self.pose.theta)

            #Publishing the vel_msg
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
	    

	    while  sqrt(pow((coordinate[j][0] - self.pose.x), 2) + pow((coordinate[j][1] - self.pose.y), 2)) >= distance_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
                vel_msg.linear.x = 0.5 * sqrt(pow((coordinate[j][0] - self.pose.x), 2) + pow((coordinate[j][1] - self.pose.y), 2))
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
	        vel_msg.angular.z = 0

 	        self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

          
            #Stopping our robot after the movement is over
            vel_msg.linear.x = 0
            vel_msg.angular.z =0
            self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        x = TurtleBot()
        x.move2goal()

    except rospy.ROSInterruptException: pass
