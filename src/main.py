from app import init_app
from userland.helpers import print_msg

# https://www.psycopg.org/psycopg3/docs/api/errors.html#psycopg.DataError
# https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/

def main() -> int:
	"""App main function.
		:return: A status code.
		:rtype: int
	"""
	print_msg("Welcome to this test project!")
	init_app()
	return 0

if __name__ == "__main__":
	main()
