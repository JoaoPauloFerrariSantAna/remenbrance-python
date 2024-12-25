from userland.checks import is_over_limit, is_acc_blocked, does_acc_exists
from userland.helpers import get_user_info, print_msg
from userland.profile import to_profile
from custom_types import OpStatus, UserData
from operation_statuses import OpErrors, OpSuccess
from locks import FieldLimits

def login_acc() -> OpStatus:
	"""Will try to login into account.
		:return: Status code that will indicate if login in was OK
		or there was errors in the way.
		:rtype: OpStatus.
	"""
	user_data: UserData = get_user_info()

	if(is_acc_blocked(user_data[0], user_data[1])):
		return OpErrors.ACC_IS_BLOCKED

	if(is_over_limit(user_data[0], FieldLimits.NAME_MAX_LENGTH) or
		is_over_limit(user_data[1], FieldLimits.EMAIL_MAX_LENGTH)):
		print_msg("Oh! Your name or email is too long to create an account!.")
		return OpErrors.MAX_LENGTH_REACHED

	to_profile(user_data[0], user_data[1])
	return OpSuccess.ACC_OK

