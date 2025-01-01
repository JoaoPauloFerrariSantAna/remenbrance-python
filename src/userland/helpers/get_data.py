from timestamps import get_curr_date
from custom_types import UserId, UserData, ReminderInformation
from www.sql import select

def get_uid(uname: str, umail: str) -> UserId:
	"""Function to get user id.
	:param uname: Username.
	:param umail: user email.
	:type uname: string.
	:type umail: string.
	:return: The user id.
	:rtype: UserId.
	"""
	stmt: str = "user_id FROM user_tbl WHERE user_name = $1 AND user_email = $2"
	stmt_types: str = "VARCHAR(16), VARCHAR(32)"
	params: str = f"'{uname}', '{umail}'"
	uid: tuple[UserId] = select(stmt, stmt_types, params)

	return uid[0]

def get_user_info() -> UserData:
	"""Will get user information.
	:return: Returns a list containing username and user email.
	:rtype: UserData.
	"""
	print("Account name.")
	print(">>> ", end='')
	name = input()

	print("Account email.")
	print(">>> ", end='')
	email = input()

	print("Account password.")
	print(">>> ", end='')
	passwd = input()

	return (name, email, passwd, get_curr_date("%Y-%m-%d %H:%M:%S.%f"))

def get_reminders_details() -> ReminderInformation:
	"""Will get the reminder details.
	:return: Returns a list of the reminder details.
	:rtype: ReminderInformation.
	"""
	rdata = get_curr_date("%Y-%m-%d %H:%M:%S.%f")
	rtitle = input("Reminder's title: ")
	rdesc = input("Reminder's description: ")
	return (rdata, rtitle, rdesc)
