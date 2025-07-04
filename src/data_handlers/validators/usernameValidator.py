from locks import FieldLimits

class UsernameValidator():
	def __init__(self, username: str) -> None:
		self.__validate_username_length(username)
		self.__username = username

	def __validate_username_length(self, username) -> None:
		try:
			if(username > FieldLimits.NAME_MAX_LENGTH):
				raise RuntimeError(f"INPUTED NAME EXCEEDS FIELD LIMIT ({FieldLimits.NAME_MAX_LENGTH} chars)")
		except RuntimeError as err:
			print("An error occurred:",err)

	def get_username(self) -> str:
		return self.__username
