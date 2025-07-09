from custom_data.exceptions import FieldLengthException
from locks import FieldLimits

class UsernameValidator():
	def __init__(self, username: str) -> None:
		self.__validate_username_length(len(username))
		self.__username = username

	def __validate_username_length(self, username) -> None:
		limit = FieldLimits.NAME_MAX_LENGTH

		try:
			if(username > limit):
				raise FieldLengthException
		except FieldLengthException as err:
			raise

	def get_username(self) -> str:
		return self.__username
