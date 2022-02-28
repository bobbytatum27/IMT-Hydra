from ..sensor import Sensor

import serial
import time
from threading import Timer

class Sita(Sensor):
	"""
    Sita class which inherits from Sensor
	
    Attributes
    ----------
    
    ser: Serial
	measureTimeLimit: int
	measureInterval: int
	baud_rate: int
	port: int
	timer: Timer

    Methods
    -------
    
    power_on()
  		turns on the SITA by making a serial connection
	power_off()
  		turn off the SITA by closing serial connection
	write_data()
  		write sensor data to a text file in the same folder
	collect_data()
  		call write_data() every 30 minutes
    """

	# Initialize Member Variables
	def __init__(self, measureTimeLimit, measureInterval, baud_rate, port):
		self.ser = serial.Serial(self.port, self.baud_rate)
		self.measureTimeLimit = measureTimeLimit
		self.measureInterval = measureInterval
		self.baud_rate = baud_rate
		self.port = port

	def power_on(self):
		""" Power on the SITA using the serial connection """
		# powerup
        self.ser.write('\r\n:020605000100F2\r\n'.encode('utf-8'))
        time.sleep(1)
        # no cal
        self.ser.write('\r\n:020601000600F1\r\n'.encode('utf-8'))
        time.sleep(3)
        # sample
        self.ser.write('\r\n:020601000B00EC\r\n'.encode('utf-8'))
        time.sleep(1)

	def power_off(self):
		""" Power off the SITA using the serial connection """
		self.ser.write('\r\n:020605000000F3\r\n'.encode('utf-8'))
        time.sleep(0.2)
        self.ser.write('\r\n:020618000000E0\r\n'.encode('utf-8'))
        self.ser.close()
        time.sleep(2)

	def write_data(self):
		""" Write sensor SITA data to sita_log.txt in the same folder """
		fdata = open('sita_log.txt','at')   
		sampled = False
        measureStart = time.time()
        while not sampled:
            # query
            self.ser.write('\r\n:020618000500DB\r\n'.encode('utf-8'))
            time.sleep(0.04)
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                now = time.time()
                if len(line) > 20:
                    print(time.ctime(now)+' @ '+line+'\r\n')
                    fdata.write(time.ctime(now)+' @ '+line+'\r\n')
                    sampled = True
                else:
                    if now > measureStart + self.measureTimeLimit:
                        print(time.ctime(now)+' @ SITA measurement timeout\r\n')
                        fdata.write(time.ctime(now)+' @ SITA measurement timeout\r\n')                     
                        sampled = True

	def collect_data(self):
		""" Check the serial connection, collect data, and write data every 30 minutes """
		# sanity check of serial connection
		self.ser.flush()
		if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            print(line)

		# setup timer
		self.timer = Timer(self.measureInterval, self.write_data)
		self.timer.start()
