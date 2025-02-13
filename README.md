# K1CORE challenge

## Overview

The test assignment will involve creating a simple application using Django and FastAPI.
Django will be used for the admin panel and ORM, FastAPI will be used for the API endpoints.

## General info 

You can use Postman [collection](https://www.postman.com/dimchik32/workspace/k1core/collection/25524341-10bce9fb-af46-4a20-9406-e8da8ce3b41b?action=share&creator=25524341
) to interact with API.

Swagger documentation for API: http://127.0.0.1:8000/docs

API entry point: http://127.0.0.1:8000/api/v1/

Django admin panel: http://127.0.0.1:8000/django/admin/

## Usage

1. Clone this repository
```
https://github.com/Dima12334/k1core.git
```
2. Build docker:
```
docker-compose build
```
3. Load db dump (optional):
```
docker-compose up db && docker-compose exec -T db psql -U postgres -d k1core < dump_db.sql
```
4. If you didn't load dumb, you need to apply django migrations by this command:
```
docker-compose up db redis app && docker-compose exec app python manage.py migrate
```
5. Up other docker containers:
```
docker-compose up
```
6. Setup Static Files
```
docker-compose exec app python manage.py collectstatic --noinput && docker-compose restart app
```
7. Create user
```
docker-compose exec app python manage.py createsuperuser
```
or if you loaded db dump, you can use existing user:
* **username**: ```admin```
* **password**: ```qwerty```
8. Done. Use the App.
