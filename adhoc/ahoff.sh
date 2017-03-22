#!/bin/bash

read -p "Any key to switch-off the ad-hoc" -n1 -s && echo "/n"		

# sudo systemct1 start dhcpcd.service				#*Workaround-ed in ahon.sh (dhcpcd issue?)		
sudo cp /etc/network/interfaces.backup /etc/network/interfaces	#Change interfaces(.adhoc) for interfaces.orig
sudo iwconfig wlan0 mode Managed						
sudo ifdown wlan0 && sudo ifup wlan0				#Off and on
echo "All settings restored"
