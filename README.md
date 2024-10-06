# Radiation detector

Simple project to count ticks from a radiation detector.

Inspired/stolen from
https://www.balena.io/blog/build-a-simple-radiation-monitor-using-a-raspberry-pi-influxdb-and-grafana/
and https://github.com/chrisys/background-radiation-monitor (Apache license).

# Installation

- `sudo apt-get install libpython3-dev`
- `make venv` to set up environment

# Pins

| *Geiger counter*           | *Pi GPIO header* |
| GND                        | Pin 6 (GND)      |
| 5V                         | Pin 2 (5V)       |
| VIN (note: actually data!) | Pin 7 (GPIO 4)   |


Output of `pinout` on Pi 3:

```
,--------------------------------.
| oooooooooooooooooooo J8 PoE +====
| 1ooooooooooooooooooo   12   | USB
|  Wi                    oo   +====
|  Fi  Pi Model 3B+ V1.3         |
| |D     ,---.           1o   +====
| |S     |SoC|            RUN | USB
| |I     `---'                +====
| |0               C|            |
|                  S|       +======
|                  I| |A|   |   Net
| pwr      |HDMI|  0| |u|   +======
`-| |------|    |-----|x|--------'

J8:
   3V3  (1) (2)  5V
 GPIO2  (3) (4)  5V
 GPIO3  (5) (6)  GND
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8
   GND (25) (26) GPIO7
 GPIO0 (27) (28) GPIO1
 GPIO5 (29) (30) GND
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

```
