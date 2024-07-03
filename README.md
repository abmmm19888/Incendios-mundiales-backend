# Blog's Backend

## Installation

Python virtual environment installation and configuration.

	sudo apt install python3.10-venv
	python3 -m venv venv

Required Python packages are installed inside the project's virtual environment.

	source venv/bin/activate
	pip3 install fastapi sqlalchemy psycopg2-binary uvicorn[standard] python-dotenv python-jose[cryptography] passlib[bcrypt]

## Configuration

Database docker container definition is located at `docker-compose.yaml`:

	services:
	  db:
		image: postgres
		environment:
		  POSTGRES_USER: ${DB_USER}
		  POSTGRES_PASSWORD: ${DB_PASSWORD}
		  POSTGRES_DB: ${DB_NAME}
		ports:
		  - "${DB_PORT}:${DB_PORT}"
		env_file:
		  - .env

Configuration values are located at `.env`:

	DB_USER=
	DB_PASSWORD=
	DB_NAME=
	DB_PORT=
	DB_HOST=

`JWT_SECRET_KEY` can be generated with OpenSSL:

	openssl rand -hex 32

Virtual environment files, configuration values and cached files should be added to `.gitignore` so they are not tracked:

	.env
	venv/
	__pycache__/

## Structure

`main.py` imports API routers from `routers/`, which call services (CRUD functions) from `services/` that use models from `core/models.py`. Database session creation is defined at `core/database.py` and sessions are created in routers and passed to services.

## Execution

Database is started and `main.py` is executed inside the virtual environment so `app` FastAPI object defined there can be used to serve requests.

	docker-compose up
	source venv/bin/activate
	uvicorn main:app --reload --port 8000

