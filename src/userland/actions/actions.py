from userland.queries import(
	create_account,
	update_user_data,
	set_acc_inactive,
	create_reminder,
	get_reminders_details,
)
from data_handlers.validators import(
	EmailValidator,
	PasswordValidator,
	UsernameValidator
)
from data_handlers.entities import Database, User
from timestamps import  get_curr_date
from helpers import print_user_info, print_msg
from custom_data.types import UserId, FormatedDate, UserData
from locks import UpdatableFields

def get_user_info() -> UserData:
	print("Account name.")
	print(">>> ", end='')
	name = input()
	print("Account email.")
	print(">>> ", end='')
	email = input()
	print("Account password.")
	print(">>> ", end='')
	passwd = input()

	acc_ts = get_curr_date()

	# i really don't mind this being mutable
	return [name, email, passwd, acc_ts]

def create_user() -> User:
	"""Will get user information.
	:return: Returns a list containing username and user email.
	:rtype: User instance.
	"""
	uinfo = get_user_info()
	vname: UsernameValidator = UsernameValidator(uinfo[0])
	vpass: PasswordValidator = PasswordValidator(uinfo[2])
	vmail: EmailValidator = EmailValidator(uinfo[1])

	print_msg(f"Registering user...\nAccount created at {0} UTC".format(get_curr_date("%d/%m/%Y %H:%M")))
	uid = create_account(
		vname.get_username(),
		email.get_email(),
		vpass.get_password(),
		uinfo[3]
	)
	user = User(vname, vmail, vpass, uinfo[3])

	return user

def make_reminder(uid: UserId) -> None:
	"""Will create a reminder.
		:param uid: The user id.
		:type uid: UserId.
		:return: None.
	"""
	rinfo = get_reminders_details()

	print_msg("CREATING POST...")
	create_reminder(uid, rinfo)
	print_msg("DONE: POST WAS CREATED SUCCESSFULLY!")

def update_field(user: User) -> None:
	"""It will update user information (username, email or password).
		:param user: The user to update the information.
		:type user: User.
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
	"""It will deactivate the user account.
	:param uid: The user id to use to delete the account.
	:type uid: UserId.
	:return: None.
	"""
	print_msg("Are you sure? (y/n)")
	op = input("(DeleteAccount)>>> ")

	if(op == 'Y'):
		set_acc_inactive(uid)

def check_info(user: User) -> None:
	"""It will show infomation belonging to the user.
		:param user: The user to show information.
		:return None.
	"""
	# i could just use a __repr__ here, but i want to do stuff the hard way :v
	print_user_info(user.get_username(), user.get_email(), user.get_timestamp())
	print_msg("Would you like to [u]pdate or [g]o back?")

	print(">>> ", end='')
	op = input()

	if(op == 'u'):
		update_field(user)
