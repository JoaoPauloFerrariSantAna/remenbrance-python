class Reminder():
	def __init__(self, title: str, description: str, creation_data):
		self.__title = title
		self.__description = description
		self.__creation_data = creation_date
	
	def set_title(self, reminder_title) -> None:
		self.__title = reminder_title
	
	def set_description(self, reminder_description) -> None:
		self.__description = reminder_description
	
	def set_data(self, reminder_creation_date) -> None:
		self.__creation_data = reminder_creation_date
	
	def make_reminder(self) -> None:
		print("")
