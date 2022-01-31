from enum import Enum

# TODO(bobbytatum27): Header to explain Glider States (and who cares about them)
class State(Enum):
	LOW_POWER = 1
	Quiescent = 2
	Storm = 3
	WAVEBREAK = 4