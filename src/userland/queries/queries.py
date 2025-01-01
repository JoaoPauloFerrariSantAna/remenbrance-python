from custom_types import UserId, UserData, ReminderInformation, FormatedDate
from timestamps import get_curr_date
from locks import UpdatableFields
from www.sql import update, select, insert

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
	stmt = f"user_tbl SET user_{field_name} = $1 WHERE user_id = $2"
	stmt_params = "(VARCHAR(32), INTEGER)"
	updated_info = f"'{new_data}', '{uid}'"
	update(stmt, stmt_params, updated_info)

def set_acc_inactive(uid: UserId) -> None:
	"""Will set account inactive.
	:param uid: The user id account to inactivate.
	:type uid: UserId.
	:return: None.
	"""
	current_date = get_curr_date("%Y-%m-%d %H:%M:%S.%f")
	stmt = f"user_tbl SET is_active = 'false', deleted_at = '{current_date}' WHERE user_id = $1"
	stmt_params = "(INTEGER)"
	user_to_deactivate = f"'{uid}'"
	update(stmt, stmt_params, user_to_deactivate)

def create_reminder(uid: UserId, rinfo: ReminderInformation) -> None:
	"""Will create a reminder.
		:param uid: The user account id to use as FK.
		:param rinfo: Post information.
		:type uid: UserId.
		:type rinfo: ReminderInformation.
		:return: None.
	"""
	stmt = "reminder_tbl(rtitle, rdesc, created_at, user_id) VALUES($1, $2, $3, $4)"
	stmt_params = "VARCHAR(32), VARCHAR(32), DATE, INTEGER"
	post_data = f"'{rinfo[1]}', '{rinfo[2]}', CURRENT_TIMESTAMP, {uid}"
	insert(stmt, stmt_params, post_data)

def create_account(name: str, email: str, passwd: str, timestamp: FormatedDate) -> None:
	"""Will create an account register.
	:param name: The user name.
	:param email: The user email.
	:param passwd: The user password.
	:param timestamp: The timestamp of when the account was created.
	:type name: str.
	:type email: str.
	:type passwd: str.
	:type timestamp: FormatedDate.
	:return: None.
	"""
	stmt: str = "user_tbl(user_name, user_email, created_at, user_passwd) VALUES($1, $2, $3, $4)"
	dtypes: str = "(VARCHAR(16), VARCHAR(32), TIMESTAMP, VARCHAR(16))"
	user_info: str = f"'{name}', '{email}', '{timestamp}', '{passwd}'"
	insert(stmt, dtypes, user_info)
