from custom_data.exceptions import FieldLengthException
from locks import FieldLimits

class EmailValidator():
	def __init__(self, email: str) -> None:
		self.__validate_email_length(len(email))
		self.__email = email
	
	def __validate_email_length(self, length: int) -> None:
		limit = FieldLimits.EMAIL_MAX_LENGTH

		try:
			if(length > limit):
				raise FieldLengthException
		except FieldLengthException as err:
			raise
	
	def get_email(self) -> str:
		return self.__email
