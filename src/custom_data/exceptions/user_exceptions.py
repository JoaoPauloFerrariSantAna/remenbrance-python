class FieldLengthException(Exception):
	"""
		Exception for the case of overflow from given field.
		Meant to be thrown when given input exceeds limit.
	"""
	default_message = "Input has overflown."

	def __init__(self) -> None:
		super().__init__(default_message)
