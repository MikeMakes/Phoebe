#!/bin/bash


#############################	Description	######################################

#Turn off Ad-Hoc and restore the previous wlan configuration
#Used with ahon.sh is a easy way for tongle the Ad-Hoc


#############################	Useful things and error handling	##############

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Commentable in case it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}

	
#############################	The script starts here	##############################

#Check what RPi is this
PI=false
grep 'BCM2708' /proc/cpuinfo && PI=true
grep 'BCM2709' /proc/cpuinfo && PI=true


if [ "$PI" = false ]; then sudo stop network-manager; fi		#In case the PC use network-manager
#Restore interface config and removing backup
sudo cp /etc/network/interfaces.backup /etc/network/interfaces || error_exit "$LINENO: I couldn't restore the backup"
sudo rm /etc/network/interfaces.backup
sudo iwconfig wlan0 mode Managed


#Turning off and on the interface
sudo ifdown wlan0 
sudo ifup wlan0
if [ "$PI" = false ]; then sudo start network-manager; fi		#In case the PC use network-manager
sudo iwlist wlan0 scan
sudo iwconfig
echo "All settings restored" && exit 0
