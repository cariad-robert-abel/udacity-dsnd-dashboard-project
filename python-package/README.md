# SQL Query API

This directory contains the `employee_events` package, which provides
an API to query the employee events database.

## Entity Relaitonship Diagram

```mermaid
erDiagram

  employee {
    INTEGER index
    INTEGER employee_id
    TEXT first_name
    TEXT last_name
    INTEGER team_id
  }

  employee_events {
    INTEGER index
    TEXT event_date
    INTEGER employee_id
    INTEGER team_id
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER index
    INTEGER employee_id
    INTEGER team_id
    TEXT note
    TEXT note_date
  }

  team {
    INTEGER index
    INTEGER team_id
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }
```

## License

Original files Copyright 2012–2020 Udacity, Inc.
My additions to documentation and code are [MIT](https://spdx.org/licenses/MIT).
See [LICENSE-Udacity](../LICENSE-Udacity) resp. [LICENSE](../LICENSE).
