# Django Rest Framework Projects

## Overview

This repository contains multiple Django projects, each prefixed with gs, that demonstrate various aspects of Django Rest Framework (DRF) for API development. These projects cover a range of functionalities and use cases.

---

## gs1

### Overview

`gs1` is a Django project that showcases the implementation of basic CRUD operations using Django Rest Framework. It includes custom views and serializers for handling API requests.

### Current Work

- **Set Up DRF**: Integrated Django Rest Framework for API management.
- **CRUD Endpoints**: Implemented endpoints for Create, Read, Update, and Delete operations.
- **Custom Views**: Developed custom views to handle API interactions.
- **Serializer Implementation**: Used DRF serializers for data validation and processing.

### Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd gs1
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

6. **Access the API**
    Visit `http://127.0.0.1:8000/` to interact with the API endpoints.

---

## gs2

### Overview

`gs2` is a Django project using Django Rest Framework to manage student records through a custom API endpoint. This project emphasizes handling JSON data and custom error handling.

### Current Work

- **Custom API Endpoint**: Developed an endpoint `/stucreate/` for creating student records.
- **JSON Data Handling**: Implemented parsing of JSON data from requests and rendering of JSON responses.
- **Error Handling**: Added mechanisms for handling invalid data and exceptions.
- **CSRF Exemption**: Disabled CSRF protection for testing purposes.

### Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd gs2
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

6. **Test the API Endpoint**
    Use `myapp.py` or any HTTP client to send a POST request to `http://127.0.0.1:8000/stucreate/` with JSON data.
    ```python
    import requests

    URL = 'http://127.0.0.1:8000/stucreate/'
    data = { name: 'Andrew', roll: 101, city: 'Hanger' }
    response = requests.post(URL, json=data)
    print(response.json())
    ```
## gs3

### Overview

`gs3` is a Django project that extends the capabilities of API development with Django Rest Framework by providing a unified API endpoint for managing student data. This project includes advanced data handling, error management, and supports CRUD operations (GET, POST, PUT, DELETE) on student records. It also integrates CSRF exemption for testing purposes.

### Current Work

- **Unified API Endpoint**: Developed a single endpoint `/studentapi/` to handle CRUD operations for student records.
- **Data Handling**: Implemented parsing and rendering of JSON data, with comprehensive error handling for invalid data and non-existent records.
- **CRUD Operations**: Enabled Create, Read, Update, and Delete operations through the API.
- **CSRF Exemption**: Disabled CSRF protection to simplify testing and development.

### Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd gs3
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

6. **Test the API Endpoint**
    You can test the API using `myapp1.py` or any HTTP client. Here are examples of how to interact with the API:

    - **GET Request**
        ```python
        import requests

        url = 'http://127.0.0.1:8000/studentapi/'
        response = requests.get(url, params={'id': 1})
        print('GET Response:', response.json())
        ```

    - **POST Request**
        ```python
        import requests
        import json

        url = 'http://127.0.0.1:8000/studentapi/'
        data = {
            'name': 'Jason',
            'roll': 4,
            'city': 'Kota'
        }
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        print('POST Response:', response.json())
        ```

    - **PUT Request**
        ```python
        import requests
        import json

        url = 'http://127.0.0.1:8000/studentapi/'
        data = {
            'id': 4,
            'name': 'Trudo',
            'city': 'Agra'
        }
        response = requests.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        print('PUT Response:', response.json())
        ```

    - **DELETE Request**
        ```python
        import requests
        import json

        url = 'http://127.0.0.1:8000/studentapi/'
        data = {
            'id': 4
        }
        response = requests.delete(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        print('DELETE Response:', response.json())
        ```

### Known Issues

- **Database Table Not Found**: Ensure migrations are applied and the database schema is correctly set up.
- **CSRF Exemption**: CSRF protection is disabled for testing purposes; consider enabling it for production environments.
# gs4

## Overview

`gs4` is a Django-based REST API application designed to manage student data efficiently. Built using Django 5.1.1 and Django Rest Framework 3.15.2, this project demonstrates advanced data handling and validation techniques, including CRUD operations, custom field-level validation, and object-level validation to ensure data integrity.

## Current Work

- **CRUD Operations:** Provides endpoints for creating, retrieving, updating, and deleting student records.
- **Custom Field-Level Validation:** Ensures that student names start with 'R'.
- **Object-Level Validation:** Validates that if the student's name is 'Lauren', the city must be 'Faridabad'.
- **Error Handling:** Includes specific error messages for validation failures.

## Setup Instructions

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gs4.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gs4
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (if needed):

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### GET `/studentapi/`

- **Description:** Retrieve a list of student records or a specific student by ID.
- **Parameters:**
  - `id` (optional): ID of the student to retrieve.

### POST `/studentapi/`

- **Description:** Create a new student record.
- **Payload:**
  ```json

### PUT `/studentapi/`

- **Description:** Update an existing student record.
- **Payload:**
  ```json
  {
    "id": 1,
    "name": "Updated Name",
    "roll": 456,
    "city": "Updated City"
  }
  
### DELETE `/studentapi/`

- **Description:** Delete a student record.
- **Payload:**
  ```json
  {
    "id": 1
  }

  {
    "name": "Student Name",
    "roll": 123,
    "city": "City Name"
  }

## Known Issues

- Ensure the `name` field starts with 'R' to pass validation.
- If the `name` is 'abc', the `city` must be 'xyz' to pass object-level validation.
- The `roll` field should be less than `xxx`; otherwise, it will raise a 'Seat Full' error.
