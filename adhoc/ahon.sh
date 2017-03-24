#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}
	
#############################	The script starts here	##############################


echo "Backup /etc/network/interfaces as interfaces.backup"
sudo cp /etc/network/interfaces /etc/network/interfaces.backup || error_exit "$LINENO: Error here!"

#Wait a key to be pressed && Working in that /n
read -p "Any key to switch-on the ad-hoc" -n1 -s && echo "/n"		

#Change interfaces for interfaces.adhoc
sudo cp $DIR/interfaces.adhoc /etc/network/interfaces || error_exit "$LINENO: Error here!"
#sudo iwconfig wlan0 key off

sudo ifdown wlan0 && sudo ifup wlan0	#Turning off and on the interface
sudo ifdown wlan0 && sudo ifup wlan0	#Twice for actually get it working (dhcpcd issue maybe?)
echo "Ad-Hoc ready" && exit 0

