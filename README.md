# Backend

## Installation and execution

Install Docker and use `docker-compose` to create database and API containers (you can open two tabs):

	docker-compose up db
	docker-compose up api

## Structure documentation

Users interact with the frontend website and call this API, which uses a PostgreSQL database to store data. API and DB are isolated using Docker containers, which are like lightweight virtual machines.

Configuration variables used by `docker-compose` are in `.env`. If any configuration variable is changed, all affected containers should be ran again.

`JWT_SECRET_KEY` can be generated with OpenSSL:

	openssl rand -hex 32

`Dockerfile` contains the commands needed in order to create API Docker images. Python packages required by the API are listed in `requirements.txt`.

Configuration variables and cached files should be added to `.gitignore` so they are not tracked:

	.env
	__pycache__/

