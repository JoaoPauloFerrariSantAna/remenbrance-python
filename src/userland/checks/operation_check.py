from userland.helpers import print_msg
from custom_types import OpStatus, QueryResult

def check_for_none(query_result: QueryResult, op_name: str) -> None:
	if(query_result is None):
		print_msg(f"\t\t\tPANICK:\nSomething went wrong during operation {op_name}!")
		print_msg("CLOSING APP!")
		exit(1)

def check_op_exit_code(op_exit_code: OpStatus, err_op_code: OpStatus, msg: str) -> None:
	"""Function will check if the exit code of the function is of a error code.
		:param op_exit_code: The exit code of the operation.
		:param 	err_op_code: The error code to check against.
		:type op_exit_code: OpStatus.
		:type err_op_code: OpStatus.
		:return: None.
	"""
	if(op_exit_code == err_op_code):
		print_msg(msg)

