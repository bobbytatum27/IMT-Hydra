from abc import ABC, abstractmethod

class Sensor(ABC):

	# Abstract Methods

	@abstractmethod
	def power_on(self):
		...

	@abstractmethod
	def power_off(self):
		...

	@abstractmethod
	def write_data(self, filehandler):
		...

	@abstractmethod
	def collect_data(self):
		...