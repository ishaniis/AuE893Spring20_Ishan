This folder will contain three programs, 
The first program is meant to navigate the turtle into a circle, with the file named as circle.py

Second program would focus on navigating the turtle into a straight line.

Lastly, the last program would be based on navigating the turtle into a square closed loop for the given set of coordinates. In the third 
program using the concept of 'Odometry' and Euclidean Distance, we have able to achieve the objectivity of the given program.

In all the three program, body of the coding and specifically initially body elements of the code are analogous. 

Standard elements adopted for all the three codes: 

importing the dependencies in form of the relevant python libraries.
First, Foremost to make the code executable, the shebank is used to effectively run the code on the shell. 
It's an effective way to instruct the Operating system i.e - Linux 16.04 in our case that the file in reference is a code in python.
How did you get this shebank ? Wondered How ? (Just type - 'which python' this would effectively answer your question.

Now, after declaration of the shebank, the code proceeds into effectively address the dependencies of a given program by importing the 
required libary for the given program.
If anytime, you feel your system doesn't have the required libraries, you can always install them using PIP, it's the standard package manager for python.

If you don't have pip package you can that easily by typing -
1. Step1 - sudo apt-get install python-pip 
2. Step2 - pip install <Package name>
  
Now, when you have made sure that the dependencies of the given code have been solved. You can proceed to importing the libraries into you code. 

Now, as we move ahead, we proceed to the body of the code for the given program. 
Process adopted which strikes commonality in all the three codes (circle.py , square_openloop.py , square_closedloop.py) 
1. Step 1 - Starting a new Node
2. Step 2 - Creating a Publisher (to lead communications to the turtlebot)(Moreof, a clinical example of widely used messaging system in DevOps and different network architectures (Commonly used tools - Apache Kafka) )
3. Step 3 - Creation of message 
ROS effectively utilizes the messages to describe data values that need to be published onto the nodes during the entire process.
4. Step 4 - Establishing the publish rate

Rest, the body of the code changes from this end for all the three programs. 
To ease off the entire process, the series of steps has been encapsulated in one function, as it gives you an advantage to effectively work through the series of steps just by calling the above defined function once.

Steps to run the scripts -
rosrun turtlesim <node_name>
python <script name>

**POINT OF ERROR -
If you have upgraded your python IDE environment to 3.6 or above (to the Latest 3.7). I would STRONGLY RECOMMEND to downgrade your environment for the fact the ROS Kinetic stable release as of now seems compatible to just 2.7.2 release only.
To check the environment version 
1. python --version
 **After you install the python 2.7.2, make sure to configure the environment accurately with the required variables. 
