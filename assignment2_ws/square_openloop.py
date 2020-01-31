#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from math import radians

def move():
	# Starts a new node
        rospy.init_node('turtlesim_node', anonymous=True)

        # Create a publisher which can "talk" to Turtlesim and tell it to move
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
	        
	#So, we have to deal with two types of motions,
	#first the linear motion in a straight line and then 
	#turning over at 90 degrees and then moving ahead
        #This message creation will be to move ahead with no angular velocity
        # Create a Twist message and add linear x
        move_cmd = Twist()
        move_cmd.linear.x = 0.2
        move_cmd.angular.z = 0.0

        # Save current time and set publish rate at 10 Hz
        now = rospy.Time.now()
        rate = rospy.Rate(5)

	#This will be our second twist variable, i.e turn
        turn_cmd = Twist()
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(45) 
	#45 deg/s in radians/s

	#two keep drawing squares.  
	#Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
	count = 0
        while not rospy.is_shutdown():
	    # go forward 0.4 m (2 seconds * 0.2 m / seconds)
	    	rospy.loginfo("Going Straight")
            	for x in range(0,10):
                	pub.publish(move_cmd)
                	rate.sleep()
	    		# turn 90 degrees
	    		rospy.loginfo("Turning")
            	for x in range(0,10):
                	pub.publish(turn_cmd)
                	rate.sleep()            
	    	count = count + 1
		if(count == 4):
			count=0
		if(count == 0):
			rospy.loginfo("Turtlebot close to its starting point")
	   
        
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass


