from enum import IntEnum

class OpErrors(IntEnum):
	ACC_IS_BLOCKED = -1
	ACC_ALREADY_EXISTS = -2
	MAX_LENGTH_REACHED = -3
