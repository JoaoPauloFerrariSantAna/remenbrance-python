from userland.form import reg_acc, login_acc
from userland.checks import check_op_exit_code

def init_app() -> None:
	"""Will run main app.
		:return: None.
	"""
	op: str = ' '

	# when translating, please use a "do-while" if possible
	while(op != 'e'):
		print("Would you like to [c]reate or [l]ogin into a account or [e]xit app?", end = ' ')
		op = input()

		if(op == 'c'):
			reg_acc()

#		if(op == 'l'):
#			login_acc()
