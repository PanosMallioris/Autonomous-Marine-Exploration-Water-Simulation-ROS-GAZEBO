# Autonomous Marine Exploration Water Simulation ROS GAZEBO

To simulate the project follow this instructions:

In a new terminal access your catkin workspace.

# $ cd catkin_ws/src
# $ git clone https://github.com/PanosMallioris/Autonomous-Marine-Exploration-Water-Simulation-ROS-GAZEBO.git
# $ cd ..
# $ catkin_make

If the catkin make is successfull proceed.

# $ roscore

In a new terminal

# $ roslaunch auv ocean.launch

This should open the simulation world

# Tip! If you get an error like 
# [ocean.launch] is neither a launch file in package [auv] nor is [auv] a launch file name
# The traceback for the exception was written to the log file
 Try 
# $ source ~/catkin_ws/devel/setup.bash
 and then launch again.

You will have to spawn the vessel in the desired position through the launch

In a new terminal

# $ roslaunch auv spawn_auv.launch

If you want to initiate the python for the autonomous exploration, Make sure you pressed the play button on Gazebo:
(Note the python script is made for the particular's map propotions and size its not perfect but its good enough for the proof of concept)

# $ cd catkin_ws/src
# $ python auv_safe.py

To stop the script press Control + C in the terminal.

If you want to teleop the robot through the world 

# $ roslauch auv auv_teleop.launch

# FOR THE SIMULATION I MADE A SECOND WORLD YOU CAN ALSO TRY OUT

Follow the same instructions just change
# $ roslaunch auv ocean.launch
to
# $ roslaunch auv marine.launch

and run the python script

# $ python auv_marine.py 
 
instead.








