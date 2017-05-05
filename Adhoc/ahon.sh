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
	echo "Backup alredy exist. Ad-Hoc probably on, trying to turn it off"
	.$DIR/ahoff.sh
else
	echo "Backup /etc/network/interfaces as interfaces.backup"
	sudo cp /etc/network/interfaces /etc/network/interfaces.backup || error_exit "$LINENO: Error creating backup"
fi

#Check what RPi is this
grep '3989d85a' /proc/cpuinfo && PI=pi3MIGUEL 
grep 'some numbers from grep Serial /proc/cpuinfo' /proc/cpuinfo && PI=pi3OTHER
grep '0010' /proc/cpuinfo && PI=pi1OTHER

echo " Setting /etc/network/interfaces properly"	#Change interfaces for interfaces.adhoc
if [ "$PI" = "pi3MIGUEL" ]; then 
	sudo cp $DIR/interfaces.adhocpi3MIGUEL /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocpi3 to /etc/network"
elif [ "$PI" != "pi3MIGUEL" ]; then
	sudo cp $DIR/interfaces.adhocpiXOTHER /etc/network/interfaces || error_exit "$LINENO: Error copying  .adhocpiXOTHER to /etc/network"
else
	error_exit "$LINENO: I dont know what RPi is in use. Check the README if you dont know what I am talking about"
fi

sudo ifdown wlan0 && sudo ifup wlan0
sudo ifdown wlan0 && sudo ifup wlan0				#Twice for actually get it working properly (?)
echo "Restarting inteface wlan0. This gonna take me 20s"	#Waiting for the interface establishment
sleep 20
iwlist wlan0 scan						#Scan with wlan0 (Somes drivers need this to trigger IBSS)

echo "Ad-Hoc ready" && exit 0

