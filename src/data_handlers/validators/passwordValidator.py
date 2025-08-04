from custom_data.exceptions import FieldLengthException
from locks import FieldLimits

class PasswordValidator():
	def __init__(self, password: str) -> None:
		self.__validate_password_length(len(password))
		self.__password = password
	
	def __validate_password_length(self, password: int) -> None:
		limit = FieldLimits.PASSWD_MAX_LENGTH

		if(password > limit):
			raise FieldLengthException
	
	def get_password(self) -> str:
		return self.__password

