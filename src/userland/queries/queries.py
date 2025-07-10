from data_handlers.entities import Database
from custom_data.types import UserId, ReminderInformation, FormatedDate
from timestamps import get_curr_date
from locks import UpdatableFields

def update_user_data(field_name: str, new_data: str, uid: UserId) -> None:
	"""Updates field user data`.
	:param field: Field to update.
	:param updated_info: Changed name, email or password.
	:param uid: The user id used to search in Database.
	:type field: UpdatableFields.
	:type updated_info: string.
	:type uid: UserId.
	:return: None.
	"""
	dbh = Database()

	stmt = f"user_tbl SET user_{field_name} = $1 WHERE user_id = $2"
	stmt_params = "(VARCHAR(32), INTEGER)"
	updated_info = f"'{new_data}', '{uid}'"

	dbh.update(stmt, stmt_params, updated_info)

def set_acc_inactive(uid: UserId) -> None:
	"""Will set account inactive.
		:param uid: The user id account to inactivate.
		:type uid: UserId.
		:return: None.
	"""
	dbh = Database()

	current_date = get_curr_date()
	stmt = f"user_tbl SET is_active = 'false', deleted_at = '{current_date}' WHERE user_id = $1"
	stmt_params = "(INTEGER)"

	dbh.update(stmt, stmt_params, f"'{uid}'")

def create_reminder(uid: UserId, rinfo: ReminderInformation) -> None:
	"""Will create a reminder.
		:param uid: The user account id to use as FK.
		:param rinfo: Post information.
		:type uid: UserId.
		:type rinfo: ReminderInformation.
		:return: None.
	"""
	dbh = Database()

	stmt = "reminder_tbl(rtitle, rdesc, created_at, user_id) VALUES($1, $2, $3, $4)"
	stmt_params = "VARCHAR(32), VARCHAR(32), DATE, INTEGER"
	post_data = f"'{rinfo[1]}', '{rinfo[2]}', CURRENT_TIMESTAMP, {uid}"

	dbh.insert(stmt, stmt_params, post_data)

def get_user_id(name: str, email: str) -> UserId:
	"""Function to use solemny in the login."""
	dbh = Database()

	stmt = "user_id, created_at FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	dtypes = "(VARCHAR(16), VARCHAR(32))"
	user_info = f"'{name}', '{email}'"

	data = dbh.select(stmt, dtypes, user_info)

	return data

def create_account(name: str, email: str, passwd: str, timestamp: FormatedDate) -> UserId:
	"""Will create an account register.
		:param name: The user name.
		:param email: The user email.
		:param passwd: The user password.
		:param timestamp: The timestamp of when the account was created.
		:type name: str.
		:type email: str.
		:type passwd: str.
		:type timestamp: FormatedDate.
		:return: the user id.
	"""
	dbh = Database()

	stmt = "user_tbl(user_name, user_email, created_at, user_passwd) VALUES($1, $2, $3, $4) RETURNING id"
	dtypes = "(VARCHAR(16), VARCHAR(32), TIMESTAMP, VARCHAR(16))"
	user_info = f"'{name}', '{email}', '{timestamp}', '{passwd}'"

	uid = dbh.insert(stmt, dtypes, user_info)

	return uid
