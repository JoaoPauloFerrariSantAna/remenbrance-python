from psycopg2 import connect, OperationalError
from .helpers import print_err_msg
from custom_types import EnvInfo

def get_db_env() -> EnvInfo:
	"""Returns db env info."""
	DB_NAME = "leaf"
	USR = "leaf"
	PASSWD = "d3f?4lt8seR"
	PORT = "5432"
	HOST = "localhost"

	return (HOST, DB_NAME, USR, PASSWD, PORT)

def db_connect():
	"""Will connect to the DB.
	:returns: A database connection.
	"""
	db_env: EnvInfo = get_db_env()
	conn = None

	try:
		conn = connect(f"""
					host='{db_env[0]}'
					dbname='{db_env[1]}'
					user='{db_env[2]}'
					password='{db_env[3]}'
					port='{db_env[4]}'
				""")
	except(Exception, OperationalError) as err:
		print_err_msg(err)

	return conn
