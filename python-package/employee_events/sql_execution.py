from sqlite3 import connect
from pathlib import Path
from functools import wraps
from importlib.resources import files
from typing import Any

import pandas as pd

__all__ = (
    'QueryMixin',
    'query',
)

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
# package/anchor may only be omitted from Python 3.12
EMPLOYEE_DB_PATH = Path(files(__package__).joinpath('employee_events.db'))


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:

    def pandas_query(self, sql_query: str) -> pd.DataFrame:
        """
        Executes an SQL query and returns the result as a pandas DataFrame.

        Parameters:
            sql_query: The SQL query to execute.
        Returns:
            The result of the query as a pandas DataFrame.
        """
        connection = connect(EMPLOYEE_DB_PATH)
        df = pd.read_sql_query(sql_query, connection)
        connection.close()
        return df

    def query(self, sql_query) -> list[tuple[Any]]:
        """
        Executes an SQL query and returns the result as a list of tuples.

        Parameters:
            sql_query: The SQL query to execute.
        Returns:
            List of tuples, one for each row of data.
        """
        connection = connect(EMPLOYEE_DB_PATH)
        cursor = connection.execute(sql_query)
        return cursor.fetchall()


# Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(EMPLOYEE_DB_PATH)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result

    return run_query
