#!/bin/sh

/mnt/us/python3/bin/python3.9 /mnt/us/extensions/SendToKindle/receiver.py

dbus-send --system /default com.lab126.powerd.resuming int32:1