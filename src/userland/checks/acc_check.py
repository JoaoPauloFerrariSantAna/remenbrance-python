from .operation_check import check_for_none
from www.sql import select
from custom_types import QueryResult

def is_acc_blocked(uname: str, umail: str) -> bool:
	"""Function that checks if account is blocked.
		:param uname: Username.
		:param umail: User email.
		:type uname: string.
		:type umail: string.
		:return: True if `is_active` is `f`, False if the contrary.
		:rtype: bool.
	"""
	stmt: str = "is_active FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	acc_info: str = f"'{uname}', '{umail}'"

	status: QueryResult = select(stmt, stmt_types, acc_info)

	check_for_none(status, "account status")
	return status[0] == False

def does_acc_exists(uname: str, umail: str) -> bool:
	"""Function that checks if account exist or not.
		:param uname: Username.
		:param umail: User email.
		:type uname: string.
		:type umail: string.
		:return: True if the `count` returns 1, False if `count` finds another
				account with the same username and email.
		:rtype: bool.
	"""
	stmt: str = "count(*) FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	acc_info: str = f"'{uname}', '{umail}'"

	amount_users: QueryResult = select(stmt, stmt_types, acc_info)
	check_for_none(amount_users, "account existence")
	return amount_users[0] == 1

