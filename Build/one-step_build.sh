#!/bin/bash


#############################	Description	######################################

#One- Step build
#This script should install and setup all dependencies in your raspberry pi


#############################	Useful things and error handling	##############

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Comment this line if it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}


#############################	The script starts here	##############################

sudo apt-get update

echo "Checking if vlc is installed (and installing it if it''s not), since it would be used as the rtsp client" 
vlc --version || sudo apt-get install vlc

echo "Checking if picamera library is installed (and installing it if it''s not)" 
python -c "import evdev" || sudo apt-get install python-evdev
