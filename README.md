# Django Demo API App 

## Overview

It built on Django Rest Framework and utilizing Postgres SQL Database. Basic CURD operations Django DRF app.

## Prerequisites

- Python 3.10.x
- PostgreSQL (Exit the app/settings.py)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/mrankitvish/django-drf-demo-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-drf-demo-app/app
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    # On Windows
    .\venv\Scripts\activate

    # On Linux/Mac
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access your app at [http://localhost:8000/](http://localhost:8000/)


