from abc import ABC, abstractmethod

# TODO(bobbytatum27): Class header, method headers
class Sensor(ABC):

	# Abstract Methods

	@abstractmethod
	def power_on(self):
		pass

	@abstractmethod
	def power_off(self):
		pass

	@abstractmethod
	def write_data(self, filehandler):
		pass

	@abstractmethod
	def collect_data(self):
		pass