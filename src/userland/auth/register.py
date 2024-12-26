from userland.checks import is_over_limit, is_acc_blocked, does_acc_exists
from userland.helpers import get_user_info, print_msg
from userland.profile import to_profile
from custom_types import OpStatus, UserData
from operation_statuses import OpErrors, OpSuccess
from locks import FieldLimits
from timestamps import get_curr_ts
from www.sql import insert

def reg_acc() -> OpStatus:
	"""Will try to register user.
		:return: Status code that will indicate if account creation was OK
		or there was errors in the way.
		:rtype: OpStatus.
	"""
	user: UserData = get_user_info()

	stmt: str = "user_tbl(user_name, user_email, created_at) VALUES($1, $2, $3)"
	dtypes: str = "(VARCHAR(16), VARCHAR(32), TIMESTAMP)"
	user_info: str = f"'{user[0]}', '{user[1]}', '{user[2]}'"

	if(is_over_limit(user[0], FieldLimits.NAME_MAX_LENGTH) or
		is_over_limit(user[1], FieldLimits.EMAIL_MAX_LENGTH)):
		print_msg("Oh! Your name or email is too long to create an account!.")
		return OpErrors.MAX_LENGTH_REACHED

	if(does_acc_exists(user[0], user[1])):
		print("There is already someone with that username.")
		return OpErrors.ACC_ALREADY_EXISTS

	print_msg(f"Registering user...\nAccount created at {get_curr_ts()}")
	create_account(user_data[0], user_data[1], user_data[2], user_data[3])
	to_profile(get_uid(user_data[0], user_data[1]), user_data[0], user_data[1], user_data[2], user_data[3])

	return OpSuccess.ACC_OK
