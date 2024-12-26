from custom_types import OpStatus, UserId
from userland.actions import check_info, deactivate_acc, make_reminder
from userland.helpers import get_uid, print_msg, print_options
from operation_statuses import OpSuccess
from timestamps import get_curr_day

def to_profile(uid: UserId, uname: str, umail: str, passwd: str, acc_ts: FormatedDate) -> OpStatus:
	"""Will run userspace.
		:param uname: Username typed in login or reg_user.
		:param umail: User email typed in login or reg_user.
		:type uname: string.
		:type umail: string.
		:return: A status code that says if the user exited or deleted account.
		:rtype: OpStatus.
	"""
	uid: UserId = get_uid(uname, umail)
	print_msg(f"Hello {uname}! Today is {get_curr_day()}.")

	# add a do-while loop here, later on
	while(True):
		print_options()
		op: str = input(">>> ")

		if(op == 'M'):
			make_reminder(uid)

		if(op == 'C'):
			check_info(uid)
			continue

		if(op == 'L'):
			break

		if(op == 'D'):
			print_msg("Deleting account...")
			deactivate_acc(uid)
			return OpSuccess.ACC_DELETED_SUCCESSFULY

	return OpSuccess.USER_EXIT
