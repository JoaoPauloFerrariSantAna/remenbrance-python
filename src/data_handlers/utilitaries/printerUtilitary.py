from sys import stderr
from custom_data.types import FormatedDate

class PrinterUtilitary():
	@staticmethod
	def print_msg(msg: str) -> None:
		"""Function to show formated message.
		:param msg: The message to show.
		:type msg: string.
		:return: None."""
		print()
		print("----------------------")
		print(msg)
		print("----------------------")
		print()

	@staticmethod
	def print_err_msg(msg: str) -> None:
		"""Function to show formated error message.
		:param msg: The message to show.
		:type msg: string.
		:return: None."""
		stderr.write("----------------------\n")
		stderr.write(msg)
		stderr.write("----------------------\n")
		stderr.flush()

	@staticmethod
	def print_options() -> None:
		"""Function to show what the user can do.
		:return: None."""
		print("Would you like to:")
		print(">>[M]ake a post.")
		print(">>[C]heck account information.")
		print(">>[D]elete account.")
		print(">>[L]ogout")

	@staticmethod
	def print_user_info(name, email, acc_ts: FormatedDate) -> None:
		"""Will show the fields which user can edit.
		:param uinfo: User information obtained from get_credentials.
		:param acc_ts: User account creation date.
		:type uinfo: UserData.
		:type acc_ts: FormatedDate.
		:return: None."""
		print_msg(f"\t\t\tACCOUNT INFO:\n- Username: {name}.\n- User email: {email}.\n- Creation date: {acc_ts}.")
