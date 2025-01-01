from typing import Any
from .prepare import send_select_query

def select(stmt: str, query_types: str, data: str) -> Any:
	"""Will make an select query.
		:param data: The rest of the query after COMMAND select
		:type data: str.
		:return: The selected data.
		:rtype: Any.
	"""
	query = ' '.join(["SELECT", stmt])
	result = send_select_query(query, query_types, data)

	return result
