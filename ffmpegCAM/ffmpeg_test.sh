#!/bin/bash


#############################	Description	######################################

#Test ffmpeg saving a test file named output.h264 on the current folder


#############################	Useful things and error handling	##############

#Check what RPi is this
PI=false
grep 'BCM2708' /proc/cpuinfo && PI=true
grep 'BCM2709' /proc/cpuinfo && PI=true

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Commentable in case it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org):

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}

#############################	The script starts here	##############################

ffmpeg -f v4l2 -framerate 16 -video_size 640x480 -i $DIR output.h264  || error_exit "$LINENO: Ooops, something wrong, the test didnt even initiate? Check your ffmpeg installation"
