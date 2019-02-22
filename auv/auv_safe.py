import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

def scan_callback(msg):
   global g_range_ahead
   global l_range
   global r_range
   g_range_ahead = min(msg.ranges)
   r_range = msg.ranges[0]
   l_range = msg.ranges[189]
   print "min range ahead : %0.1f" % g_range_ahead
   print "range left : %0.1f" % l_range
   print "range right : %0.1f" % r_range
   print len(msg.ranges)

g_range_ahead = 1 # anything to start
scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('wander')
#state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)# rythmos ektelesis tou controller


while not rospy.is_shutdown():
  
  twist = Twist()
  if (l_range >= 1 and r_range >=1 and g_range_ahead >=1) :#driving_forward:
    # BEGIN FORWARD
    twist.linear.x = 0.6 
    cmd_vel_pub.publish(twist)
  else :
     if r_range < 8:
         twist.angular.z = 1.5 #turn left
         twist.linear.x=0.25
         cmd_vel_pub.publish(twist)
         time.sleep(0.1)
         twist.angular.z = 0
      #driving_forward = False
      #state_change_time = rospy.Time.now() + rospy.Duration(1)
      # END FORWARD
     elif r_range > 8  :
         twist.angular.z = -1.5 #turn right
         cmd_vel_pub.publish(twist)
         time.sleep(0.1) # we're not driving_forward
         twist.angular.z=0
     
    
     else :
         twist.linear.x= 0.2
         cmd_vel_pub.publish(twist) 
         time.sleep(0.5)
         twist.linear.x= 0.0
         twist.angular.z = 0.0
  #cmd_vel_pub.publish(twist)

  rate.sleep()# xronos ypologismenos apo ro ROS anamesa sta loop
# END ALL
