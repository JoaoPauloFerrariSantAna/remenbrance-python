from datetime import datetime, timezone, timedelta
from custom_types import FormatedDate

def get_curr_date(fmt: str) -> FormatedDate:
	"""Will get the current date in UTC format.
	:param fmt: The date format to use.
	:returns: A formated datetime.
	"""
	current_date = datetime.now(timezone(timedelta(0)))

	return current_date.strftime(fmt)
