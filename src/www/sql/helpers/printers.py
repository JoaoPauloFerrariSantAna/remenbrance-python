import sys

def print_err_msg(msg: str) -> None:
	sys.stderr.write("----------------------\n")
	sys.stderr.write(str(msg))
	sys.stderr.write("----------------------\n")
	sys.stderr.flush()
