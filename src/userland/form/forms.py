from helpers import print_msg
from userland.profile import to_profile
from userland.actions import create_user
from userland.checks import is_acc_blocked, does_acc_exists


def reg_acc() -> None:
	"""Will try to register user."""
	print("Work on validation")
	print("like... to see if the account already exists")
	exit(1)
	user = create_user()

	# if(does_acc_exists(user.get_user_id(), user.get_username())):
		# print("There is already someone with that username.")

	# to_profile(user)

def login_acc() -> None:
	"""Will try to login into account.
		:return: Status code that will indicate if login in was OK
		or there was errors in the way.
		:rtype: OpStatus.
	"""
	print("Work on validating the id next")
	print("To see if the account was already blocked")
	exit(1)
	user = set_user() 

#	if(is_acc_blocked(user_data[0], user_data[1])):
#		return OpErrors.ACC_IS_BLOCKED

#	to_profile(user)
