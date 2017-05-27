#!/bin/bash


#############################	Description	######################################

#One- Step build
#This script should install and setup all dependencies in your raspberry pi



#############################	The script starts here	##############################

sudo apt-get update

echo "Checking if vlc is installed (and installing it if it''s not), since it would be used as the rtsp client" 
vlc --version || sudo apt-get install vlc

echo "Checking evdev library (gamepad input)" 
INSTALL_EVDEV = false
python -c "import evdev" || INSTALL_EVDEV = true
if [ "$INSTALL_EVDEV" = true ]; then 
	sudo apt-get install python-dev python-pip gcc
	sudo apt-get install linux-headers-$(uname -r)
	pip install evdev
fi

echo "Checking socket library (used for TCP connection)"
python -c "import socket" || sudo apt-get install python-socket
