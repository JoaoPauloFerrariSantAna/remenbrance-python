from timestamps import get_curr_ts
from custom_types import UserId, UserData, ReminderInformation
from www.sql import select

def get_uid(uname: str, umail: str) -> UserId:
	"""Function to get the user id from DB.
		:param uname: Username.
		:param umail: user email.
		:type uname: string.
		:type umail: string.
		:return: The user id that the user with `uname` and `umail` has.
		:rtype: UserId.
	"""
	stmt: str = "user_id FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	params: str = f"'{uname}', '{umail}'"
	uid: tuple[UserId] = select(stmt, stmt_types, params)

	return uid[0]

def get_user_info() -> UserData:
	"""Will get user information.
		:return: Will return a list containing username and user email.
		:rtype: UserData.
	"""
	name = input("Account name: ")
	email = input("Email: ")
	return (name, email, get_curr_ts())

# TODO: add return type
def get_reminders_details() -> ReminderInformation:
	rdata = get_curr_ts()
	rtitle = input("Reminder's title: ")
	rdesc = input("Reminder's description: ")
	return (rdata, rtitle, rdesc)
