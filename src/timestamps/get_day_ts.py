from datetime import datetime, timezone, timedelta
from custom_types import FormatedDate

def get_curr_day() -> FormatedDate:
	"""
	Gets the current day.
	:returns: A date in the format "DAY (day of week)".
	:rtype: FormatedDate.
	Example of get_curr_day:
	>>> get_curr_day()
	'29 (Sunday)'
	"""
	day_utc = datetime.now(timezone(timedelta(0)))
	return day_utc.strftime("%d (%A)")

def get_curr_ts() -> FormatedDate:
	"""Gets the current timestamp.
	:returns: A date in the format of "YEAR-MONTH-DAY HOUR:MONTH:SECONDS.MICROSECONDS".
	"""
	curr_date = datetime.today()
	return curr_date.strftime("%Y-%m-%d %H:%M:%S.%f")


