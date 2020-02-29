#!\usr\bin\python
import rospy
import math
import sys
import time

from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler as tft
from math import radians
from std_msgs.msg import String

def listener():
	rospy.init_node('Listener Node', anonymous=True)
	rospy.Subscriber("chatter",string,callback)
	rospy.spin()

def setup():
	# Starts a new node
        rospy.init_node('robot_cleaner', anonymous=True)

        # Create a publisher which can "talk" to Turtlesim and tell it to move
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
	
	# Save current time and set publish rate at 10 Hz
        now = rospy.Time.now()
        rate = rospy.Rate(0.1)
	
	linear_speed = 0.5
	goal_distance = 3.0
	angular_speed = 0.5
	goal_angle = radians(180)
	setup.tf_listener = listener()
			
	rospy.sleep(2)
	setup.odom_frame = '/odom'
	
	
	setup.tf_listener.waitForTransform(setup.odom_frame, '/base_footprint', rospy.Time(), rospy.Duration(1.0))
        setup.base_frame = '/base_footprint'
	setup.tf_listener.waitForTransform(setup.odom_frame, '/base_link', rospy.Time(), rospy.Duration(1.0))
        setup.base_frame = '/base_link'

          
	rospy.loginfo("NO transform b/w /odom & /base_link or /base_footprint")
        rospy.signal_shutdown("tf Exception")  

	
	# Initialize the position variable as a Point type
	position = Point()

    	# Loop once for each leg of the trip
    	for i in range(2):
        	# Initialize the movement command
        	move_cmd = Twist()

        	# Set the movement command to forward motion
        	move_cmd.linear.x = linear_speed

        	# Get the starting position values     
        	(position, rotation) = setup.get_odom()
        	x_start = position.x
        	y_start = position.y

	# Keep track of the distance travelled
        distance = 0

        # Enter the loop to move along a side
        while distance < goal_distance and not rospy.is_shutdown():        
         	setup.cmd_vel.publish(move_cmd)
	 	r.sleep()

	# Get the current position
	(position, rotation) = setup.get_odom()

        # Compute the Euclidean distance from the start
        distance = sqrt(pow((position.x - x_start), 2) + 
                            pow((position.y - y_start), 2))

        # Stop the robot before the rotation
        move_cmd = Twist()
        setup.cmd_vel.publish(move_cmd)
        rospy.sleep(1)

        # Set the movement command to a rotation
        move_cmd.angular.z = angular_speed

        # Track the last angle measured
        last_angle = rotation

        # Track how far we have turned
        turn_angle = 0

        while abs(turn_angle + angular_tolerance) < abs(goal_angle) and not rospy.is_shutdown():
            # Publish the Twist message and sleep 1 cycle         
            setup.cmd_vel.publish(move_cmd)
            rospy.sleep()

            # Get the current rotation
            (position, rotation) = setup.get_odom()

            # Compute the amount of rotation since the last loop
            delta_angle = normalize_angle(rotation - last_angle)

            # Add to the running total
            turn_angle += delta_angle
            last_angle = rotation

        # Stop the robot before the next leg
        move_cmd = Twist()
        setup.cmd_vel.publish(move_cmd)
        rospy.sleep(1)

    	# Stop the robot for good
    	setup.cmd_vel.publish(Twist())

def get_odom(setup):
    # Get the current transform between the odom and base frames
    try:
        (trans, rot)  = setup.tf_listener.lookupTransform(setup.odom_frame, setup.base_frame, rospy.Time(0))
    except (tft.Exception, tft.ConnectivityException, tft.LookupException):
        rospy.loginfo("TF Exception")
        return

    return (Point(*trans), quat_to_angle(Quaternion(*rot)))

def shutdown(setup):
    # Always stop the robot when shutting down the node.
    rospy.loginfo("Stopping the robot...")
    setup.cmd_vel.publish(Twist())
    rospy.sleep(1)

if __name__ == '__main__':
	listener()    
	setup()
else:
    rospy.loginfo("Out-and-Back node terminated.")
