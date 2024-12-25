def is_over_limit(uinput: str, limit: int) -> bool:
	"""Function that will check if inputed data is over limit.
		:param uinput: Data given by the user.
		:param limit: Field limit in DB.
		:return: True if `uinput` is bigger than the limit, False if it isn't.
		:rtype: bool.
	"""
	return len(uinput) > limit
