

# Music Keyboards API
=======================

Welcome to the Music Keyboards API! This API allows you to list and rate music keyboards. Built with Django and Django Rest Framework.

## Features
------------

* List music keyboards
* Create new music keyboards
* Get details of a specific music keyboard
* Rate music keyboards

## Installation
------------

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/music-keyboards-api.git
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up the Database

```bash
python manage.py migrate
```

### Step 4: Start the Server

```bash
python manage.py runserver
```

## Usage
-----

### 1. List Music Keyboards

* **Endpoint**: `/keyboards/`
* **Method**: `GET`
* **Response**: A list of music keyboards with their details

### 2. Create Music Keyboard

* **Endpoint**: `/keyboards/`
* **Method**: `POST`
* **Request Body**: Music keyboard details (e.g., name, description, price)
* **Response**: The created music keyboard with its details

### 3. Get Music Keyboard Details

* **Endpoint**: `/keyboards/{id}/`
* **Method**: `GET`
* **Response**: The music keyboard details with the given ID

### 4. Rate Music Keyboard

* **Endpoint**: `/keyboards/{id}/rate/`
* **Method**: `POST`
* **Request Body**: Rating details (e.g., rating, review)
* **Response**: The updated music keyboard with its new rating

## Testing
---------

We use pytest for testing. To run the tests, use the following command:

```bash
pytest
```

## CI/CD
---------

We use GitHub Actions for CI/CD. The workflow is set up to run tests on every push to the `main` branch.

## Contributing
------------

Contributions are welcome! Please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License
-------

This project is licensed under the [MIT License](LICENSE).
