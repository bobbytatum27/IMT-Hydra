"""Contains all the necessary configuration aspects for the cSBC module.

Contains
- Serial constants
- Timing constants
"""

########### Serial constants ###########

# Serial port
PORT = '/dev/ttyUSB4'
# Baud rate
BAUD_RATE = 57600
# Timeout
TIMEOUT = 1

########### Timing constants ###########

# Time limit for each measurement of the SITA sensor (in seconds)
MEASURE_TIME_LIMIT = 20

# Time interval between each measurement of the SITA sensor (in seconds)
MEASURE_TIME_INTERVAL = 1800 # 30 minutes