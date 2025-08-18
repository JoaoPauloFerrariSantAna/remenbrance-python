from data_handlers.entities import Database
from data_handlers.utilitaries import TimeUtilitary
from custom_data.types import FormatedDate, UserId, ReminderInformation

def get_reminders_details() -> ReminderInformation:
	"""Will get the reminder details.
	:return: Returns a list of the reminder details.
	:rtype: ReminderInformation."""
	rdata = TimeUtilitary.get_curr_date()
	rtitle = input("Reminder's title: ")
	rdesc = input("Reminder's description: ")
	return (rdata, rtitle, rdesc)
