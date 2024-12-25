from userland.queries import update_user_data, set_acc_inactive, get_credentials, create_reminder
from userland.helpers import print_updatables_fields, print_msg, get_reminders_details
from custom_types import UserId, FormatedDate, UserData
from locks import UpdatableFields
from timestamps import get_acc_ts

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

def update_field(uid: UserId) -> None:
	"""It will update a certain field (username, email or password).
		:param uid: The user id.
		:return: None.
	"""
	while(True):
		print_msg("Which field would you like to update?\n- user[name].\n- [email] field.\n- [none].")
		field_to_update = input(">>> ")

		if(field_to_update == UpdatableFields.EMAIL):
			new_email = input("(NewEmail) >>> ")
			update_user_data(field_to_update, new_email, uid)
			continue

		if(field_to_update == UpdatableFields.USERNAME):
			new_uname = input("(NewUsername) >>> ")
			update_user_data(field_to_update, new_uname, uid)
			continue

		break

def deactivate_acc(uid: UserId) -> None:
	print_msg("Are you sure? (Y/N)")
	op = input("(DeleteAccount)>>> ")

	if(op == 'Y'):
		set_acc_inactive(uid)

def check_info(uid: UserId) -> None:
	"""It will show infomation belonging to the user.
		:param uid: the user id.
		:type uid: UserId.
		:return None.
	"""
	acc_ts: FormatedDate = get_acc_ts(uid)
	while(True):
		# this needs to be here, since we will update stuff here
		# this is the only way to refresh data to user without a class
		uinfo: UserData = get_credentials(uid)

		print_msg("Would you like to [u]pdate or [g]o back?")
		print_updatables_fields(uinfo[0], uinfo[1], acc_ts)
		op = input(">>> ")

		if(op == 'u'):
			update_field(uid)
			continue

		break
