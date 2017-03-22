#!/bin/bash

echo "Backup /etc/network/interfaces as interfaces.backup"
sudo cp /etc/network/interfaces /etc/network/interfaces.orig

read -p "Any key to switch-on the ad-hoc" -n1 -s && echo "/n"		#Wait a key to be pressed && Working in that /n

# sudo systemct1 stop dhcpcd.service					#*Workaround below and in ahoff.sh (dhcpcd issue?)
sudo cp ~/phoebe/adhoc/interfaces.adhoc /etc/network/interfaces		#Change interfaces for interfaces.adhoc

sudo ifdown wlan0 && sudo ifup wlan0					#Turning off and on the interface
sudo ifdown wlan0 && sudo ifup wlan0					#*Twice for actually get it working (dhcpcd issue maybe?)
echo "Ad-Hoc ready" 
