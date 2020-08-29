#!/usr/bin/env python3

# Source: https://github.com/balenalabs-incubator/background-radiation-monitor/blob/master/counter/counter.py

import datetime
import os
import time

import RPi.GPIO as GPIO
from collections import deque
from influxdb import InfluxDBClient

counts = deque()
hundredcount = 0
usvh_ratio = 0.00812037037037 # This is for the J305 tube

# This method fires on edge detection (the pulse from the counter board)
def countme(channel):
    global counts, hundredcount
    timestamp = datetime.datetime.now()
    counts.append(timestamp)

    # Every time we hit 100 counts, reset
    hundredcount = hundredcount + 1
    if hundredcount >= 100:
        hundredcount = 0

# Set the input with falling edge detection for geiger counter pulses
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.add_event_detect(7, GPIO.FALLING, callback=countme)


# Setup influx client
DB = 'radiation'
host = '192.168.23.254'
port = '8086'
INFLUX_USER = 'influxdb'
INFLUX_PASS = os.getenv('INFLUX_PASS')

influx_client = InfluxDBClient(host=host,
                               port=port,
                               username=INFLUX_USER,
                               password=INFLUX_PASS,
                               database=DB)

def main():
    """Main entry point
    """
    print("Creating database...")
    influx_client.create_database(DB)
    print("List of databases: {}".format(influx_client.get_list_database()))

    loop_count = 0
    usvh = 0 # µSv/h

    # In order to calculate CPM we need to store a rolling count of events in the last 60 seconds
    # This loop runs every second to update the Nixie display and removes elements from the queue
    # that are older than 60 seconds
    while True:
        loop_count = loop_count + 1

        try:
            while counts[0] < datetime.datetime.now() - datetime.timedelta(seconds=60):
                counts.popleft()
        except IndexError:
            pass # there are no records in the queue.


        if loop_count == 10:
            # Every 10th iteration (10 seconds), store a measurement in Influx
            usvh = len(counts) * usvh_ratio
            measurements = [
                {
                    'measurement': 'balena-sense',
                    'fields': {
                        'cpm': int(len(counts)),
                        'usvh': float("{:.2f}".format(usvh))
                    }
                }
            ]

            influx_client.write_points(measurements)
            loop_count = 0

            # Update the displays with a zero-padded string
        text_count = f"{len(counts):0>3}"
        print("COUNT: {}".format(text_count))
        print("USVH: {:.2f}".format(usvh))

        time.sleep(1)

if __name__ == '__main__':
    main()
