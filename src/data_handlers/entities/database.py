import os
# from psycopg2 import connect, OperationalError, DatabaseError
# from dotenv import load_dotenv
from helpers import print_err_msg
from custom_types import PreparedQuery, PreparedTypes, QueryResult

# load_dotenv()

class Database():
	def __init__(self) -> None:
		self.__databaseName = os.getenv("DB_NAME")
		self.__databaseUser = os.getenv("DB_USR")
		self.__databasePassword = os.getenv("DB_PASSWD")
		self.__databasePort = os.getenv("DB_PORT")
		self.__databaseHost = os.getenv("DB_HOST")

	def __connect(self):
		"""Will connect to the DB.
		:returns: A database connection.
		"""
		connection = None

		try:
			connection = connect(
				"host='{0}' dbname='{1}' user='{2}' password='{3}' port='{4}'"
				.format(self.__databaseHost, self.__databaseName,
						self.__databaseUser, self.__databasePassword, self.__databasePort
				)
			)
		except(Exception,  OperationalError) as err:
			print_err_msg("Something went wrong while connecting to DB")

		return connection
	
	def __disconnect(self, connection) -> None:
		connection.close();

	# NOTE: this and __sendSelectQuery are the same
	# i could add a flag here and this would eliminate a method 
	def __sendQuery(self, stmt: PreparedQuery, stmt_types: PreparedTypes, data: str) -> None:
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
		connection = self.__connect();
		cursor = connection.cursor()

		try:
			cursor.execute(' '.join(["PREPARE query", stmt_types, " AS", stmt]))
			cursor.execute(''.join(["EXECUTE query(", data, ')']))
			cursor.execute("DEALLOCATE query")
			cursor.close()
		except(Exception, DatabaseError) as err:
			print_err_msg("Something went wrong while tryinging to execute error")

		self.__disconnect(connection)
		connection = None

	def __sendSelectQuery(self, stmt: PreparedQuery, stmt_types: PreparedTypes, data: str) -> QueryResult:
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
		connection = self.__connect()
		cursor = connection.cursor()
		result = None

		try:
			cursor.execute(' '.join(["PREPARE select_plan(",stmt_types,") AS", stmt]))
			cursor.execute(''.join(["EXECUTE select_plan(", data, ')']))
			result = cursor.fetchone()
			cursor.execute("DEALLOCATE select_plan")
			cursor.close()
		except(Exception, DatabaseError) as err:
			print_err_msg("Something went wrong with query!")

		self.__disconnect(connection)
		connection = None
		return result

	def insert(self, stmt: str, query_types: str, data: str) -> None:
		"""Will make an insert query.
			:param data: Information to send to DB with INSERT.
			:type data: string.
			:return: None.
		"""
		query = ' '.join(["INSERT INTO", stmt])
		self.__sendQuery(query, query_types, data)

	def update(self, stmt: str, query_types: str, data: str) -> None:
		"""Will make an update query.
			:param data: Information to send to DB with UPDATE ONLY.
			:type data: string.
			:return: None.
		"""
		query = ' '.join(["UPDATE ONLY", stmt])
		self.__sendQuery(query, query_types, data)

	def select(self, stmt: str, query_types: str, data: str) -> QueryResult:
		"""Will make an select query.
			:param data: The rest of the query after COMMAND select
			:type data: str.
			:return: The selected data.
			:rtype: QueryResult.
		"""
		query = ' '.join(["SELECT", stmt])
		result: QueryResult = self.__sendSelectQuery(query, query_types, data)
		return result
