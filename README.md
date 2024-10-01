# EV Data API

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [API Endpoint](#api-endpoint)
4. [Linting with Pylint](#linting-with-pylint)
    - [Running Pylint](#running-pylint)
5. [Improvements](#improvements)

## Introduction

The **EV Data API** is a FastAPI-based application that provides insights into electric vehicles (EV) data. It fetches data from the Washington EV API and processes it to deliver metadata such as the average electric range per vehicle make.

## Installation

### Prerequisites
- Python 3.9 or higher
- `pip` package manager

### Steps

1. **Clone the Repository**
    

2. **Create and activate a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    
    # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Endpoint

The API has a single endpoint:

```bash
GET /ev/{year}
```

#### Example Request

```bash
curl -X GET "http://localhost:8000/ev/2022"
```

#### Example Response

```bash
[
    {
        "make":"MERCEDES-BENZ",
        "count":19,
        "average_range":0.0
    },
    {
        "make":"BMW",
        "count":33,
        "average_range":16.2
    },
    {
        "make":"MITSUBISHI",
        "count":6,
        "average_range":38.0
    }
]
```

## Linting with Pylint

### Running Pylint for one file (main.py)

```bash
pylint main.py
```

## Improvements
1. Unit Testing (with mocking)
2. Base, Dev, and Prod environments
3. CI/CD Pipeline
4. Get off Uvicorn and on to something like Gunicorn for production
5. Error handling
6. Logging
7. Rate limiting
8. Security (API keys, authentication, and authorization)
9. Dockerize
10. API versioning
11. Adding a database, ORM, and Alembic for migrations

