from custom_types import UserId, FormatedDate

# meh, I could use a struct from ctype
# but i'll me trying to do a MVC approach to this :v
class User():
	def __init__(self, user_id: UserId, username: str, email: str, password: str, account_timestamp: FormatedDate):
		self.__user_id = user_id
		self.__username = username
		self.__email = email
		self.__password = password
		self.__timestamp = account_timestamp

	def get_user_id(self) -> UserId:
		return self.__user_id

	def get_username(self) -> None:
		return self.__username

	def get_email(self) -> str:
		return self.__email

	def get_password(self) -> str:
		return self.__password

	def get_timestamp(self) -> FormatedDate:
		return self.__timestamp

	def set_username(self, new_username: str) -> None:
		self.__username = new_username

	def set_email(self, new_email: str) -> None:
		self.__email = new_email

	def set_password(self, new_password: str) -> None:
		self.__password = new_password
