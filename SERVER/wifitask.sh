#!/bin/bash

printf "\n\n************************************************************************\n" >> $(pwd)/wifi_log.txt
date >> $(pwd)/wifi_log.txt
if [ ping -q -c1 8.8.8.8 &>/dev/null ]; then
    printf "The Internect connection is not active.\nReseting...\n" >> $(pwd)/wifi_log.txt

    nmcli networking off
    nmcli networking on
    
    nmcli -o >> wifi_log
   
else
    printf "Internet connection is active.\n" >> $(pwd)/wifi_log.txt
fi
