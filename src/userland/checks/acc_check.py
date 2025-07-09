from data_handlers.entities import Database
from custom_data.types import QueryResult
from .operation_check import check_for_none

# NOTE: from what i've done, this whole file can go to some validator

def is_acc_blocked(uname: str, umail: str) -> bool:
	"""Function that checks if account is blocked.
		:param uname: Username.
		:param umail: User email.
		:type uname: string.
		:type umail: string.
		:return: An boolean to represent if the account is blocked or not.
		:rtype: bool.
	"""
	dbh: Database = Database()
	stmt: str = "is_active FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	acc_info: str = f"'{uname}', '{umail}'"

	status: QueryResult = dbh.select(stmt, stmt_types, acc_info)

	check_for_none(status, "account status")
	return status[0] == False

def does_acc_exists(uname: str, umail: str) -> bool:
	"""Function that checks if account exist or not.
		:param uname: Username.
		:param umail: User email.
		:type uname: string.
		:type umail: string.
		:return: An boolean to represent if the account already exits.
		:rtype: bool.
	"""
	dbh: Database = Database()
	stmt: str = "count(*) FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	acc_info: str = f"'{uname}', '{umail}'"

	amount_users: QueryResult = dbh.select(stmt, stmt_types, acc_info)
	check_for_none(amount_users, "account existence")
	return amount_users[0] == 1

