# Install and run this easily on DebAthena using
# wget http://goo.gl/SerBjI && bash SerBjI

sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
sudo apt-get install libopencv-dev python-opencv
sudo apt-get install python-pygame
git clone https://github.com/mfranzs/splash_cv_class.git
subl splash_cv_class splash_cv_class/read_webcam.py
xdg-open https://github.com/mfranzs/splash_cv_class/blob/master/README.md