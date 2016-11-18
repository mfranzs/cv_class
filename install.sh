# Install and run this easily using
# wget -O - http://goo.gl/SerBjI | bash

sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
sudo apt-get install libopencv-dev python-opencv
git clone https://github.com/mfranzs/splash_cv_class.git
cd cv_class
subl read_webcam.py
