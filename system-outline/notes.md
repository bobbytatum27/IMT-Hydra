Power measurement video on Bobby's iphone

# From Figma
Bubble Cam - storm state, active whitecap

Foam Cam - synchronized w/ bubble cam (same states, time/event synchronized)...individual images should capture pictures over same time interval of the same event (one from side, one from above)

White Cap Cam - storm state, active white cap: log data @ 1 picture / 15 min.

SITA - sample 24/7, every half hour take a sample

MET 1 - sample 24/7, every half hour (turn off during LOCKDOWN mode...windspeed exceeds pre-defined threshold)

Conductivity Sensor - part of bubble cam, foam cam, whitecap cam system...running during active storm state, constantly logging

GPS - liquid robotics, always running

Hydrophone Array - runs 24/7 independently of everything else, always logging data

Single Hydrophone (near Bubble Cam) - both storm states: continously logging

Power draw (rui), 

physical footprint(matt), 

heat sinking reqs., 

data storage reqs (bobby), 

physical interconnects for power/data (matt/bobby)
bobby: what is connected to what + how
matt: spacing/topology
to discuss: how to screw/latch ethernet cables

each subsystem has these requirements, add these to the appropriate modules...aka for every subsystem, we need to know the aforementioned bullets

Hardware List

SBCs
Raspberry Pi (Master SBC) - 5 W
Latte Panda x2
Bubble Cam
Foam Cam / White Cap Cam
Raspberry Pi (mSBC) ???

Sensors
Bubble Cam (FLIR Camera)
Foam Cam (FLIR Camera)
White Cap Cam (FLIR Camera)
SITA
MET 1
Conductivity Sensor
GPS (provided by Liquid Robotics)
Singular Hydrophone
Hydrophone Array

Networking / Connectors
Network Switch
Ethernet Cabling
Breadboard Jumper Wires
4 Port RS232 to USB Connector

Custom PCBs
Power Control Board (mark needs to deliver to lab)
