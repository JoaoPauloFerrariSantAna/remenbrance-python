from locks import FieldLimits

class EmailValidator():
	def __init__(self, email: str) -> None:
		self.__validate_email_length(email)
		self.__email = email
	
	def __validate_email_length(self, email: str) -> None:
		try:
			if(email > FieldLimits.EMAIL_MAX_LENGTH):
				raise RuntimeError(f"GIVEN EMAIL EXCEEDS FIELD LIMIT ({FieldLimits.EMAIL_MAX_LENGTH} chars)")
		except RuntimeError as err:
			print("An error occurred:",err)
	
	def get_email(self) -> str:
		return self.__email
