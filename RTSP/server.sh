#!/bin/bash


#############################	Description	######################################

#Start receiving the stream using vlc
#Future functionality; receive and save the stream in the client

#############################	Useful things and error handling	##############

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Commentable if it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}

	
#############################	The script starts here	##############################

vlc -vvv v4l2:///dev/video0 --sout '#rtp{dst=localhost,port=1234,sdp=rtsp://localhost:8080/test.sdp}'
