#!/bin/bash


#############################	Description	######################################

#One- Step build
#This script should install and setup all dependencies in your raspberry pi



#############################	The script starts here	##############################

sudo apt-get update

echo "Checking if vlc is installed (and installing it if it''s not), since it would be used as the rtsp client" 
vlc --version || sudo apt-get install vlc

echo "Checking evdev library (gamepad input)" 
python -c "import evdev" || sudo apt-get install python-evdev

echo "Checking socket library (used for TCP connection)"
python -c "import socket" || sudo apt-get install python-socket
