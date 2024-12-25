from .prepare import send_query
from .helpers import print_err_msg

def insert(stmt: str, query_types: str, data: str) -> None:
	"""Will make an insertion in DB.
		:param data: Information to send to DB with INSERT.
		:type data: string.
		:return: None.
	"""
	query = ' '.join(["INSERT INTO", stmt])
	send_query(query, query_types, data, "Oh! we could not create the requested data!")

def update(stmt: str, query_types: str, data: str) -> None:
	"""Will make an update in DB.
		:param data: Information to send to DB with UPDATE ONLY.
		:type data: string.
		:return: None.
	"""
	query = ' '.join(["UPDATE ONLY", stmt])
	send_query(query, query_types, data, "Oh! There was some problem updating your data!")
