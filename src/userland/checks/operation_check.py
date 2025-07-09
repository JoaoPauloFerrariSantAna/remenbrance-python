from helpers import print_msg
from custom_data.types import QueryResult

def check_for_none(query_result: QueryResult, op_name: str) -> None:
	if(query_result is None):
		print_msg(f"\t\t\tPANICK:\nSomething went wrong during operation {op_name}!")
		print_msg("CLOSING APP!")
		exit(1)
