from datetime import datetime, timezone, timedelta
from custom_types import FormatedDate

def get_curr_date(fmt: str) -> FormatedDate:
	current_date = datetime.now(timezone(timedelta(0)))

	return current_date.strftime(fmt)
