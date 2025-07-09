from custom_data.types import UserId, FormatedDate
from userland.actions import check_info, deactivate_acc, make_reminder
from data_handlers.entities import User
from helpers import print_msg, print_options
from timestamps import get_curr_date

def to_profile(uid: UserId, uname: str, umail: str, passwd: str, acc_ts: FormatedDate) -> None:
	"""Will run userspace.
	:param uname: Username typed in login or reg_user.
	:param umail: User email typed in login or reg_user.
	:type uname: string.
	:type umail: string.
	"""
	user: User = User(uid, uname, umail, passwd, acc_ts)
	print_msg("Hello {0}! Today is {1}.".format(uname, get_curr_date("%a (%A)")))

	# add a do-while loop here, later on
	while(True):
		print_options()
		op: str = input(">>> ")

		if(op == 'M'):
			raise NotImplementedError
			make_reminder(user.get_user_id())

		if(op == 'C'):
			check_info(user)
			continue

		if(op == 'L'):
			break

		if(op == 'D'):
			print_msg("Deleting account...")
			deactivate_acc(user.get_user_id())
			break
