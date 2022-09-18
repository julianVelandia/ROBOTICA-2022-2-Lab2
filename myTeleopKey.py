#Teleop Key
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
TERMIOS = termios

class Turlte:

    def __init__(self) -> None:
        self.linearx_vel=0
        self.lineary_vel=0

    def moveturtle(self):
        rospy.init_node('myTeleopKey',anonymous=True)
        key= str(self.getkey())[-2]
        if key == 'a':
            self.linearx_vel = -1.5
            self.lineary_vel = 0
            self.publisher(self.linearx_vel,self.lineary_vel)
        elif key =='s':
            self.lineary_vel = -1.5
            self.linearx_vel = 0
            self.publisher(self.linearx_vel,self.lineary_vel)
        elif key =='d':
            self.linearx_vel = 1.5
            self.lineary_vel = 0
            self.publisher(self.linearx_vel,self.lineary_vel)
        elif key =='w':
            self.linearx_vel = 0
            self.lineary_vel = 1.5
            self.publisher(self.linearx_vel,self.lineary_vel)
        elif key == 'r':
            self.pAbsolute()
        elif key == ' ':
            self.pRelative()
    
    def publisher(self,linearx_vel,lineary_vel):
        velPub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        velMsg = Twist()
        velMsg.linear.x = self.linearx_vel
        velMsg.linear.y = self.lineary_vel
        #velMsg.angular.z = self.angular_vel
        velPub.publish(velMsg)

    def pAbsolute(self):
        absPub = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        absMsg = absPub((5.544445),(5.544445), 0.000000)
        return absMsg

    def pRelative(self):
        relPub = rospy.ServiceProxy('/turtle1/teleport_relative',TeleportRelative)
        relMsg = relPub(0,pi)
        return relMsg

    def getkey(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c


if __name__ == '__main__':
    turtle1 = Turlte()
    while True:
        turtle1.moveturtle()
        print('moving')
