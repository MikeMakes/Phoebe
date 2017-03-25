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
sudo cp /etc/network/interfaces /etc/network/interfaces.backup || error_exit "$LINENO: Error creating backup"

#Check what RPi is this
grep 'a02082' /proc/cpuinfo && PI=pi3 
grep '0010' /proc/cpuinfo && PI=pi1

echo " Setting /etc/network/interfaces properly"	#Change interfaces for interfaces.adhoc
if [ "$PI" = "pi3" ]; then 
	sudo cp $DIR/interfaces.adhocpi3 /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocpi3 to /etc/network"
elif [ "$PI" = "pi1" ]; then
	sudo cp $DIR/interfaces.adhocpi1 /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocpi1 to /etc/network"
else
	error_exit "$LINENO: I dont know what RPi is in use. Check the README if you dont know what I am talking about"
fi

sudo ifdown wlan0 && sudo ifup wlan0
sudo ifdown wlan0 && sudo ifup wlan0				#Twice for actually get it working properly (?)
echo "Restarting inteface wlan0. This gonna take me 20s"
sleep 20
iwlist wlan0 scan									#Scan with wlan0 (Somes drivers need this to trigger IBSS)

echo "Ad-Hoc ready" && exit 0

