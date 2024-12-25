from psycopg2 import DatabaseError
from .connections import db_connect
from .helpers import print_err_msg

# this function may return something, but for now it will return nothing
def call_proc(proc_name: str) -> None:
	"""Function that will call a procedure in the database.
		:param proc_name: The proc name to be called.
		:type proc_name: string.
		:return: None.
	"""
	with db_connect() as pg:
		with pg.cursor() as cursor:
			try:
				cursor.execute(' '.join(["CALL", proc_name]))
			except(Exception, DatabaseError):
				print_err_msg("Could not execute requested functionality!")
