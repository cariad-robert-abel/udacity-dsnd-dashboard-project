from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from . import QueryBase

__all__ = (
    'Employee',
)


# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = 'employee'

    def names(self) -> list[tuple[str, int]]:
        """Return Employee Names and IDs

        Returns:
            List of tuples containing the employee name and ID.
        """
        results = self.query(
            f'SELECT employee_id, first_name, last_name FROM {self.name}'
            )

        return [(f'{first_name} {last_name}', employee_id)
                for employee_id, first_name, last_name
                in results]

    def username(self, id: int) -> str:
        """Return Employee Full Name by ID

        Args:
            id: employee ID to be queried.

        Raises:
            LookupError: If no employee is found with the given ID.
            LookupError: If multiple employees are found with the given ID.

        Returns:
            Employee full name as a string.
        """
        results = self.query(
            f'SELECT first_name, last_name FROM {self.name} WHERE {self.name}_id = {id}'
            )

        match (len(results)):
            case 0:
                raise LookupError(f'Employee with ID {id} not found')
            case 1:
                # unpack first result and join
                return ' '.join(results[0])
            case _:
                raise LookupError(f'Multiple employees ({len(results)}) found with ID {id}')

    def model_data(self, id: int) -> 'pd.DataFrame':
        """Return Sum of Employee Event Counts by ID

        Args:
            id: employee ID to be queried.

        Returns:
            DataFrame containing the sum of positive and negative employee events
            for the given ID.
        """
        return self.pandas_query(f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """)
