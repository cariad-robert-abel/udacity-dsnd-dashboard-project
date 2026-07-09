# Software Engineering for Data Scientists

This repository contains the project associated with "Deploying a Scalable Machine Learning Pipeline
in Production" Udacity course. It's a fork of Udacity's [Starter Kit](https://github.com/udacity/dsnd-dashboard-project).

This GitHub.com project is located at [cariad-robert-abel/udacity-dsnd-dashboard-project](https://github.com/cariad-robert-abel/udacity-dsnd-dashboard-project).

## Directory Layouts and Notes

Please find the directory layouts and an Entity Relationship Diagram for the
employee events database below.

### Repository Structure
```
├── assets
│   ├── model.pkl                        Pre-Trained Risk Assessment Model
│   └── report.css                       Cascaded Style Sheet for Report
├── python-package                       employee_events package
│   ├── employee_events                  
│   │   ├── __init__.py                  
│   │   ├── employee.py                  
│   │   ├── employee_events.db           
│   │   ├── query_base.py                
│   │   ├── sql_execution.py             
│   │   └── team.py                      
│   ├── pyproject.toml                   library project metadata
│   ├── setup.py                         setuptools script
│   ├── README.md                        library README
├── report                               Report Dashboard Source Code
│   ├── base_components                  
│   │   ├── __init__.py                  
│   │   ├── base_component.py            
│   │   ├── data_table.py                
│   │   ├── dropdown.py                  
│   │   ├── matplotlib_viz.py            
│   │   └── radio.py                     
│   ├── combined_components              
│   │   ├── __init__.py                  
│   │   ├── combined_component.py        
│   │   └── form_group.py                
│   ├── dashboard.py                     
│   └── utils.py                         
├── tests                                pytest test suite
│   └── test_employee_events.py          
├── pyproject.toml                       repository project metadata
├── README.md                            repository README (this file!)
```

### employee_events.db

```mermaid
erDiagram

  employee {
    INTEGER employee_id PK
    TEXT first_name
    TEXT last_name
    INTEGER team_id
    
  }

  employee_events {
    TEXT event_date
    INTEGER employee_id FK
    INTEGER team_id FK
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER employee_id PK
    INTEGER team_id PK
    TEXT note
    TEXT note_date PK
  }

  team {
    INTEGER team_id PK
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

  team ||--o{ employee_events : "team_id"
  employee ||--o{ employee_events : "employee_id"
  notes }o--o{ employee_events : ""
```

## Installation

Install using `pip install [-e] .` from the top-level repository directory.
The `employee_event` library dependency located in the `python-package` sub-directory will be picked
up and installed automatically.

## License

Original files Copyright 2012–2020 Udacity, Inc.
My additions to documentation and code are [MIT](https://spdx.org/licenses/MIT).
See [LICENSE-Udacity](LICENSE-Udacity) resp. [LICENSE](LICENSE).
