#!/bin/bash

sleep 5
sudo ifconfig wlan0 192.168.4.1
sudo systemctl restart hostapd.service
