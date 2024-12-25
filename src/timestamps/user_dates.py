from custom_types import UserId, FormatedDate
from www.sql import select

def get_acc_ts(uid: UserId) -> FormatedDate:
	"""Gets the account creation date.
	:param uid: The user id.
	:type uid: UserId.
	:returns: A date in the format of "DAY/MONTH/YEAR".
	Example of get_curr_ts:
	>>> get_acc_ts(1)
	'27/9/2024'
	"""
	stmt = """
		date_part('DAY', created_at)  || '/' ||
		date_part('MONTH', created_at) || '/' ||
		date_part('YEAR', created_at)
		FROM user_tbl WHERE user_id = $1
	"""
	stmt_type = "INTEGER"
	creation_time: tuple[FormatedDate] = select(stmt, stmt_type, str(uid))
	return creation_time[0]

