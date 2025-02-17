# Cloud Computing Project: Food Manager

This is a cloud-based food management application built with Django and PostgreSQL. It allows users to manage their food collection with a "consumed" or "not consumed" status.

## Features
- Manage foods with attributes: name, category, and consumed status.
- RESTful API for CRUD operations.
- Dockerized setup for seamless deployment.
- Uses PostgreSQL as the database backend.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)

---

## Project Overview
The **Food Manager** is designed to demonstrate fundamental concepts of cloud computing, including containerization, database integration, and RESTful API development.

---

## Technologies Used
- **Python 3.10**
- **Django 4.x**
- **PostgreSQL**
- **Docker & Docker Compose**

---

## Installation

### Prerequisites
- Docker and Docker Compose installed on your system.
- Git installed to clone the repository.

### Steps
1. Clone the repository:
```bash
git clone https://github.com/AbolfazlEsfandiariSabzevar/project-cluod
cd cloud_computing_Project
```

2. Create a .env file in the root directory with the following format:
```env
DATABASE_NAME=food_manager
DATABASE_USER=food_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=postgres_db
DATABASE_PORT=5432
```

3. Build and start the containers:
```bash
docker-compose -f docker-compose.db.yml up --build -d
docker-compose -f docker-compose.app.yml up --build -d
```
4. Running Migrations Inside the Container
```bash
docker exec -it django_app bash
```
```bash
python manage.py migrate
```
```bash
exit
```

5. Access the application:

- Django API: http://localhost:8000

---

### Usage(اگر دستور pyhton manage.py migrate اجرا بشه ما می تونیم مراحل زیر را اجرا کنیم)
1. Test the API using tools like Postman or Curl.

2. Example API requests:
- GET all foods: GET http://localhost:8000/api/foods/
- Create a food
```
POST http://localhost:8000/api/foods/
Content-Type: application/json
{
  "name": "Pizza",
  "category": "Fast Food",
  "is_consumed": true
}
```
3. To stop the application:
```bash
docker-compose down
```

## API Endpoints

| Method | Endpoint              | Description           |
|--------|-----------------------|-----------------------|
| GET    | `/api/foods/`         | List all foods        |
| POST   | `/api/foods/`         | Add a new food        |
| GET    | `/api/foods/<id>/`    | Retrieve a food       |
| PUT    | `/api/foods/<id>/`    | Update a food         |
| DELETE | `/api/foods/<id>/`    | Delete a food         |
