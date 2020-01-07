# task_book
task_book

Python version = 3.6

## Install packages for Python
### Framework Django

```
pip install django==2.2.8
```

### PostgreSQL adapter for the Python 

```
pip install psycopg2
```

## Postgresql settings
### Create database

```
CREATE DATABASE task_book;
```

### Create user

```
CREATE USER test_task WITH password '123qwerty';
```

### Grant user rights

```
GRANT ALL privileges ON DATABASE task_book TO test_task;

```
