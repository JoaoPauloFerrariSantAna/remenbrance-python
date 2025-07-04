from userland.checks import is_over_limit
from locks import FieldLimits

class PasswordValidator():
	def __init__(self, password: str) -> None:
		self.__validate_password_length(password)
		self.__password = password
	
	def __validate_password_length(self, password) -> None:
		try:
			if(is_over_limit(password, FieldLimits.PASSWD_MAX_LENGTH)):
				raise RuntimeError(f"INPUTED PAssword EXCEEDS FIELD LIMIT ({FieldLimits.PASSWD_MAX_LENGTH} chars)")
		except RuntimeError as err:
			print("An error occurred:",err)
	
	def get_password(self) -> str:
		return self.__password

