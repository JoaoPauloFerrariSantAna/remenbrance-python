from psycopg2 import DatabaseError
from .helpers import print_err_msg
from custom_types import PreparedQuery, PreparedTypes, QueryResult
from .connections import db_connect

def send_query(stmt: PreparedQuery, stmt_types: PreparedTypes, data: str) -> None:
	"""Will execute a non prepared select statement.
		:param stmt: The prepared statement query.
		:param stmt_types: Types of the actual data inside of the DB.
		:param data: Actual data to search.
		:param err_msg: The error message to give.
		:type stmt: PreparedQuery.
		:type stmt_types: PreparedTypes.
		:type data: String.
		:type err_msg: String.
	"""
	with db_connect() as pg:
		with pg.cursor() as cursor:
			try:
				cursor.execute(' '.join(["PREPARE query", stmt_types, " AS", stmt]))
				cursor.execute(''.join(["EXECUTE query(", data, ')']))
				cursor.execute("DEALLOCATE query")
			except(Exception, DatabaseError) as err:
				print_err_msg(err)

def send_select_query(stmt: PreparedQuery, stmt_types: PreparedTypes, data: str) -> QueryResult:
	"""Will execute a prepared select statement.
		:param stmt: The prepared statement query.
		:param stmt_types: Types of the actual data inside of the DB.
		:param data: Actual data to search.
		:param err_msg: The error message to give.
		:type stmt: PreparedQuery.
		:type stmt_types: PreparedTypes.
		:type data: String.
		:type err_msg: String.
	"""
	result = None

	with db_connect() as pg:
		with pg.cursor() as cursor:
			try:
				cursor.execute(' '.join(["PREPARE select_plan(",stmt_types,") AS", stmt]))
				cursor.execute(''.join(["EXECUTE select_plan(", data, ')']))
				result = cursor.fetchone()
				cursor.execute("DEALLOCATE select_plan")
			except(Exception, DatabaseError) as err:
				print_err_msg(err)

	return result
