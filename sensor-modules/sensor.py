from abc import ABC, abstractmethod

# TODO(bobbytatum27): Class header, method headers
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