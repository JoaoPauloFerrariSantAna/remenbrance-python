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
from data_handlers.utilitaries import PrinterUtilitary, TimeUtilitary
from data_handlers.entities import Database, User
from custom_data.types import UserId
from locks import UpdatableFields

def create_user() -> User:
	"""Will get user information.
	:return: A instance.
	:rtype: User instance."""
	print("Account name.")
	print(">>> ", end='')
	name = input()

	print("Account email.")
	print(">>> ", end='')
	email = input()

	print("Account password.")
	print(">>> ", end='')
	passwd = input()

	acc_ts = TimeUtilitary.get_curr_date()

	PrinterUtilitary.print_msg(
		f"Registering user...\nAccount created at {0} UTC"
		.format(TimeUtilitary.get_curr_date("%d/%m/%Y %H:%M"))
	)

	uid = create_account(
		(UsernameValidator(name)).get_username(),
		(EmailValidator(email)).get_email(),
		(PasswordValidator(passwd)).get_password(),
		acc_ts
	)

	return User(uid, vname, vmail, vpass, acc_ts)

def make_reminder(uid: UserId) -> None:
	"""Will create a reminder.
	:param uid: The user id.
	:type uid: UserId.
	:return: None."""
	rinfo = get_reminders_details()

	PrinterUtilitary.print_msg("CREATING POST...")

	create_reminder(uid, rinfo)

	PrinterUtilitary.print_msg("DONE: POST WAS CREATED SUCCESSFULLY!")

def update_field(user: User) -> None:
	"""It will update user information (username, email or password).
	:param user: The user to update the information.
	:type user: User.
	:return: None."""
	while(True):
		PrinterUtilitary.print_msg("Which field would you like to update?\n-user[name].\n-[email].\n-[none].")
		field = input(">>> ")

		if(field == UpdatableFields.EMAIL):
			update_user_data(field, user.set_email(), user.get_user_id())
			continue

		if(field == UpdatableFields.USERNAME):
			update_user_data(field, user.set_username(), user.get_user_id())
			continue

		break

def deactivate_acc(uid: UserId) -> None:
	"""It will deactivate the user account.
	:param uid: The user id to use to delete the account.
	:type uid: UserId.
	:return: None."""
	PrinterUtilitary.print_msg("Are you sure? (y/n)")

	print("(DeleteAccount)>>> ", end='')
	op = input()

	if(op == 'Y'): set_acc_inactive(uid)

def check_info(user: User) -> None:
	"""It will show infomation belonging to the user.
	:param user: The user to show information.
	:return None."""
	# i could just use a __repr__ in the class, but i want to do stuff the hard way
	PrinterUtilitary.print_user_info(user.get_username(), user.get_email(), user.get_timestamp())
	PrinterUtilitary.print_msg("Would you like to [u]pdate or [g]o back?")

	print(">>> ", end='')
	op = input()

	if(op == 'u'): update_field(user)
