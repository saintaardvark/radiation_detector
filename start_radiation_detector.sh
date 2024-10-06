#!/bin/bash

set -e

source ./.venv/bin/activate
source .secret.sh
while true ; do
	./detector.py || true
	sleep 5
done
