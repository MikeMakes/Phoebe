#!/bin/bash


#############################	Description	######################################

#Stream video to the client from server with ffmpeg


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


if [ "$PI" = true ]; then 
	ffmpeg -f v4l2 -framerate 30 -video_size 640x480 -i /dev/video0 -tune 		zerolatency -f rtp rtp://10.42.0.1:1234 & PIDFF=$!
	#chapuza. debe cerrarse el ffmpeg cuando se quiera cerrar el programa.

else
	#ffplay rtp://10.42.0.1:1234	
	ffplay udp://10.42.0.1:1234

fi

