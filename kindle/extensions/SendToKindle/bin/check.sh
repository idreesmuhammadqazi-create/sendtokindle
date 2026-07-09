#!/bin/sh

echo "PATH=$PATH" > /mnt/us/check.log

find / -name "python*" >> /mnt/us/check.log 2>&1