# Django Rest Framework Projects

## Overview

This repository contains two Django projects, `gs1` and `gs2`, demonstrating different aspects of Django Rest Framework (DRF) for API development.

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
    data = { name: 'Andrew', roll: 101, city: 'Gonda' }
    response = requests.post(URL, json=data)
    print(response.json())
    ```

### Known Issues

- **Database Table Not Found**: Ensure migrations are applied and the database schema is correctly set up.

### Contributing

Contributions are welcome! Please open issues or submit pull requests with improvements or fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to explore both projects and provide feedback or contributions. Happy coding!
