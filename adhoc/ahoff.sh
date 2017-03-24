#!/bin/bash

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Commentable in case it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}
	
#############################	The script starts here	##############################


read -p "Any key to switch-off the ad-hoc" -n1 -s && echo "/n"		

#Restore interface config
sudo cp /etc/network/interfaces.backup /etc/network/interfaces || error_exit "$LINENO: Error here!"
sudo iwconfig wlan0 mode Managed

#Turning off and on the interface
sudo ifdown wlan0 
sudo ifup wlan0
iwlist wlan0 scan
echo "All settings restored" && exit 0
