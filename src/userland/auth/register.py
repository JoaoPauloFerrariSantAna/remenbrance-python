from userland.checks import is_over_limit, is_acc_blocked, does_acc_exists
from userland.helpers import get_uid, get_user_info, print_msg
from userland.profile import to_profile
from userland.queries import create_account
from custom_types import OpStatus, UserData
from operation_statuses import OpErrors, OpSuccess
from locks import FieldLimits
from timestamps import get_curr_date
from www.sql import insert

def reg_acc() -> OpStatus:
	"""Will try to register user.
		:return: Status code that will indicate if account creation was OK
		or there was errors in the way.
		:rtype: OpStatus.
	"""
	user_data: UserData = get_user_info()

	if(is_over_limit(user_data[0], FieldLimits.NAME_MAX_LENGTH) or
		is_over_limit(user_data[1], FieldLimits.EMAIL_MAX_LENGTH) or
		is_over_limit(user_data[2], FieldLimits.PASSWD_MAX_LENGTH)):
		print_msg("Oh! Your name, password or email is too long to create an account!.")
		return OpErrors.MAX_LENGTH_REACHED

	if(does_acc_exists(user_data[0], user_data[1])):
		print("There is already someone with that username.")
		return OpErrors.ACC_ALREADY_EXISTS

	print_msg(f"Registering user...\nAccount created at {0} UTC".format(get_curr_date("%d/%m/%Y %H:%M")))
	create_account(user_data[0], user_data[1], user_data[2], user_data[3])
	to_profile(get_uid(user_data[0], user_data[1]), user_data[0], user_data[1], user_data[2], user_data[3])

	return OpSuccess.ACC_OK
