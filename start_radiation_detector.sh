#!/bin/bash

set -e

cd /home/pi/radiation_detector
source venv/bin/activate
source .secret.sh
while true ; do
	./detector.py || true
	sleep 5
done
