from custom_types import UserId, UserData, ReminderInformation
from locks import UpdatableFields
from www.sql import update, call_proc, select, insert

def get_credentials(uid: UserId) -> UserData:
	"""Will obtain the credentials stored in the DB.
		:param uid: The user id obtained earlier.
		:type uid: UserId.
		:return: The credentials (name, email, pass, etc).
		:rtype: UserData.
	"""
	stmt = "user_name, user_email FROM user_tbl WHERE user_id = $1"
	stmt_type = "INTEGER"

	credentials: UserData = select(stmt, stmt_type, str(uid))
	return credentials

def update_user_data(field_name: str, new_data: str, uid: UserId) -> None:
	"""Will update field data with param `new_data`.
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
	"""Will set `is_active` to `false` and will update `deleted_at` with current time.
		:param uid: The user id account to inactivate.
		:type uid: UserId.
		:return: None.
	"""
	call_proc(f"lock_acc({uid})")

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

def create_account(name, email, passwd, timestamp) -> None:
	stmt: str = "user_tbl(user_name, user_email, created_at, user_passwd) VALUES($1, $2, $3, $4)"
	dtypes: str = "(VARCHAR(16), VARCHAR(32), TIMESTAMP, VARCHAR(16))"
	user_info: str = f"'{name}', '{email}', '{timestamp}', '{passwd}'"

	insert(stmt, dtypes, user_info)
