#Install#
Easily install this repository on Ubuntu by using the command on the next line to download and run install.sh. Note that this will install some packages.
wget http://goo.gl/SerBjI && bash SerBjI

#OpenCV#
##Drawing##
cv2.circle(img, center=(x,y), radius=5, color=(0,0,0), thickness=3)  
cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(0,0,0))  

#Breakout Code#
##Initializing##
Put this at the top of your code:  
import breakout

##Controlling Paddle Location
breakout.set_paddle_x(paddle_x, image_width)  
Where paddle_x is a number from 0 to image_width and image_width is your camera frame size

##Launching ball
breakout.launch_ball()


#Terminal#
Kill stuck python process:  
pkill python -9
