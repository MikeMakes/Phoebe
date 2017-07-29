#!/bin/bash


#############################	Description	######################################

#Setup Ad-Hoc, differentation between RPis
#Used with ahoff.sh is a easy way for tongle the Ad-Hoc


#############################	Useful things and error handling	##############

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #Directory where this script is (Commentable in case it is not neccesary)

# A slicker error handling routine by William Shotts (www.linuxcommand.org)

PROGNAME=$(basename $0)

error_exit()
{
	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}

	
#############################	The script starts here	##############################

if [ -e /etc/network/interfaces.backup ]; then
	echo "Backup alredy exist. Ad-Hoc probably on, trying to turn it off and then continuing"
	.$DIR/ahoff.sh
else
	echo "Backup /etc/network/interfaces as interfaces.backup"
	sudo cp /etc/network/interfaces /etc/network/interfaces.backup || error_exit "$LINENO: Error creating backup"
fi


#Check what RPi is this
PI=false
grep 'BCM2708' /proc/cpuinfo && PI=true
grep 'BCM2709' /proc/cpuinfo && PI=true


echo " Setting /etc/network/interfaces properly"		#Change interfaces for interfaces.adhoc
if [ "$PI" = true ]; then 
	sudo cp $DIR/interfaces.adhocPI /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocPI to /etc/network"
else
	sudo stop network-manager		#In case the PC use GNOME or KDE	
	sudo cp $DIR/interfaces.adhocNOTPI /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocNOTPI to /etc/network"
fi


sudo ifdown wlan0 && sudo ifup wlan0
sudo ifdown wlan0 && sudo ifup wlan0				#Twice for actually get it working properly (?)
echo "Restarting inteface wlan0. This gonna take me 20s"	#Waiting for the interface establishment
sleep 20
if [ "$PI" = false ]; then sudo start network-manager; fi		#In case the PC use GNOME or KDE
sudo iwlist wlan0 scan						#Scan with wlan0 (Somes drivers need this to trigger IBSS)

sudo iwconfig
echo "Ad-Hoc ready" && exit 0

