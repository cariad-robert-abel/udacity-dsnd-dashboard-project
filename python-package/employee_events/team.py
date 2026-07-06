from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from . import QueryBase

__all__ = (
    'Team',
)


# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = 'team'

    def names(self) -> list[tuple[str, int]]:
        """Return Team Names and IDs

        Returns:
            List of tuples containing the team name and ID.
        """
        return self.query(
            f'SELECT team_name, team_id FROM {self.name}'
            )

    def username(self, id: int) -> str:
        """Return Team Name by ID

        Args:
            id: team ID to be queried.

        Raises:
            LookupError: If no team is found with the given ID.
            LookupError: If multiple teams are found with the given ID.

        Returns:
            Team name as a string.
        """
        results = self.query(
            f'SELECT team_name FROM {self.name} WHERE {self.name}_id = {id}'
            )

        match (len(results)):
            case 0:
                raise LookupError(f'Team with ID {id} not found')
            case 1:
                # unpack first result and join
                return ' '.join(results[0])
            case _:
                raise LookupError(f'Multiple teams ({len(results)}) found with ID {id}')

    def model_data(self, id: int) -> 'pd.DataFrame':
        """Return Sum of Employee Event Counts in Team by ID

        Args:
            id: team ID to be queried.

        Returns:
            DataFrame containing the sum of positive and negative employee events
            for each employee of the given team ID.
        """
        return self.pandas_query(f"""
            SELECT positive_events, negative_events FROM (
                SELECT employee_id
                       , SUM(positive_events) positive_events
                       , SUM(negative_events) negative_events
                FROM {self.name}
                JOIN employee_events USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY employee_id
            )
            """)
