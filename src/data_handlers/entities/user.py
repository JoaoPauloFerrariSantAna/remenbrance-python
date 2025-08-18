from custom_data.types import UserId, FormatedDate
from ..validators import(
	UsernameValidator,
	EmailValidator,
	PasswordValidator
)

# https://www.youtube.com/watch?v=YGNH71KPIes

class User():
	def __init__(self, user_id: UserId, username: UsernameValidator, email: EmailValidator, password: PasswordValidator, timestamp: FormatedDate):
		self.__user_id = user_id
		self.__username = username
		self.__email = email
		self.__password = password
		self.__timestamp = timestamp

	def get_user_id(self) -> UserId: return self.__user_id
	def get_username(self) -> str: return self.__username.get_username()
	def get_email(self) -> str: return self.__email.get_email()
	def get_password(self) -> str: return self.__password.get_password()
	def get_timestamp(self) -> FormatedDate: return self.__timestamp

	def set_username(self) -> str:
		print("(NewUsername)>>> ", end='')
		nuname = input()
		vuname = UsernameValidator(nuname)
		self.__username = vuname
		return vuname.get_username()

	def set_email(self) -> str:
		print("(NewEmail)>>> ", end='')
		nemail = input()
		vemail = EmailValidator(nemail)
		self.__email = vemail
		return vemail.get_email()
