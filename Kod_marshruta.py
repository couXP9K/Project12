import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)


navigate(x=0, y=0, z=1, frame_id="body", auto_arm=True)
rospy.sleep(5)

navigate(frame_id='aruco_1', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_3', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_7', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_4', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_8', x=0, y=0, z=1)
rospy.sleep(3)

navigate(frame_id='aruco_11', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_15', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_12', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_8', x=0, y=0, z=1)
rospy.sleep(5)

navigate(frame_id='aruco_4', x=0, y=-1, z=1)
rospy.sleep(5)



land()