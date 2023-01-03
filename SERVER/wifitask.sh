#!/bin/bash


printf "\n\n************************************************************************\n" >> /home/dawid/wifi_task/wifi_log.txt
date >> /home/dawid/wifi_task/wifi_log.txt

if [[ "$(ping -c 1 8.8.8.8 | grep '100% packet loss' )" != "" ]]; then
    printf "The Internect connection is not active.\nReseting...\n" >> /home/dawid/wifi_task/wifi_log.txt

    nmcli networking off
    nmcli networking on
    
    nmcli -o >> wifi_log
   
    # exit 1
else
    printf "Internet connection is active.\n" >> /home/dawid/wifi_task/wifi_log.txt
fi
