from userland.queries import update_user_data, set_acc_inactive, create_reminder
from userland.helpers import print_user_info, print_msg, get_reminders_details
from custom_types import UserId, FormatedDate, UserData
from locks import UpdatableFields
from timestamps import get_acc_ts
from objects import User

def make_reminder(uid: UserId) -> None:
	"""Will make a post.
		:param uid: The user id.
		:type uid: UserId.
		:return: None.
	"""
	rinfo = get_reminders_details()

	print_msg("CREATING POST...")
	create_reminder(uid, rinfo)
	print_msg("DONE: POST WAS CREATED SUCCESSFULLY!")

def update_field(user: User) -> None:
	"""It will update a certain field (username, email or password).
		:param uid: The user id.
		:return: None.
	"""
	while(True):
		print_msg("Which field would you like to update?\n- user[name].\n- [email] field.\n- [none].")
		field_to_update = input(">>> ")

		if(field_to_update == UpdatableFields.EMAIL):
			new_email = input("(NewEmail) >>> ")
			user.set_email(new_email)
			update_user_data(field_to_update, new_email, user.get_user_id())
			continue

		if(field_to_update == UpdatableFields.USERNAME):
			new_uname = input("(NewUsername) >>> ")
			user.set_username(new_uname)
			update_user_data(field_to_update, new_uname, user.get_user_id())
			continue

		break

def deactivate_acc(uid: UserId) -> None:
	print_msg("Are you sure? (Y/N)")
	op = input("(DeleteAccount)>>> ")

	if(op == 'Y'):
		set_acc_inactive(uid)

def check_info(user: User) -> None:
	"""It will show infomation belonging to the user.
		:param uid: the user id.
		:type uid: UserId.
		:return None.
	"""
	print_user_info(user.get_username(), user.get_email(), user.get_timestamp())

	print_msg("Would you like to [u]pdate or [g]o back?")

	print(">>> ", end='')
	op = input()

	if(op == 'u'):
		update_field(user)
