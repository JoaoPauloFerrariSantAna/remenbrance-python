from data_handlers.entities import Database
from timestamps import get_curr_date
from custom_data.types import FormatedDate, UserId, ReminderInformation

def get_reminders_details() -> ReminderInformation:
	"""Will get the reminder details.
	:return: Returns a list of the reminder details.
	:rtype: ReminderInformation.
	"""
	rdata = get_curr_date()
	rtitle = input("Reminder's title: ")
	rdesc = input("Reminder's description: ")
	return (rdata, rtitle, rdesc)
