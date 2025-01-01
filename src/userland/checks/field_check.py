def is_over_limit(uinput: str, limit: int) -> bool:
	"""Will check if value went over limit.
		:param uinput: Data given by the user.
		:param limit: Field limit in DB.
		:return: An boolean that represents if `uinput` is over limit.
		:rtype: bool.
	"""
	return len(uinput) > limit
