from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from . import QueryMixin


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ''
    """Table name """

    def names(self) -> list[tuple[str, int]]:
        """Return Entity Names and IDs

        Returns:
            List of tuples containing the entity name and ID.
        """
        return []

    def event_counts(self, id: int) -> 'pd.DataFrame':
        """
        Count the number of positive and negative employee events by date for a
        given Team or Employee by ID.

        Args:
            id: employee or team ID to be queried.

        Returns:
            DataFrame containing the event counts for the given ID.
        """

        return self.pandas_query(f"""\
SELECT
  ee.event_date
  , SUM(ee.positive_events) AS positive_events
  , SUM(ee.negative_events) AS negative_events
FROM {self.name}
JOIN employee_events AS ee USING({self.name}_id)
WHERE {self.name}.{self.name}_id = {id}
GROUP BY ee.event_date
ORDER BY ee.event_date ASC
""")

    def notes(self, id: int) -> 'pd.DataFrame':
        """Retrieve all Notes for a given Team or Employee by ID.

        Args:
            id: employee or team ID to be queried.

        Returns:
            DataFrame containing the notes for the given ID.
        """

        return self.pandas_query(f"""\
SELECT
  n.note_date
  , n.note
FROM notes AS n
JOIN {self.name} USING({self.name}_id)
WHERE {self.name}.{self.name}_id = {id}
ORDER BY n.note_date ASC
""")
