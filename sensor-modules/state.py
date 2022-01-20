from enum import Enum

# TODO(bobbytatum27): Header to explain Glider States (and who cares about them)
class State(Enum):
	Quiescent = 1
	Storm = 2
	Event = 3