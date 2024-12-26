from custom_types import UserId
# meh, I could use a struct from ctype
# but i'll me trying to do a MVC approach to this :v
class User():
	def __init__(user_id: UserId, username: str, email: str, password: str):
		self.__user_id = user_id
		self.__username = username
		self.__email = email
		self.__password = password

	def get_user_id(self) -> UserId:
		return self.__user_id

	def set_username(self, new_username: str) -> None:
		self.__username = new_username

	def set_email(self, new_email: str) -> None:
		self.__email = new_email

	def set_password(self, new_password: str) -> None:
		self.__password = new_password
	
