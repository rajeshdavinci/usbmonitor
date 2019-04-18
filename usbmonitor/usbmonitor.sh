#!/bin/bash
set -x
mkdir -p /opt/usb-notifier
xauthority=$(printenv | grep XAUTHORITY | cut -d = -f 2)
sed -i  "9i Environment=XAUTHORITY=$xauthority" usbmonitor.service 
cp usbmonitor.service /lib/systemd/system
systemctl daemon-reload
systemctl enable usbmonitor
systemctl start usbmonitor
