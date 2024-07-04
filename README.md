# Backend

## Installation and execution

Install Docker and use `docker-compose` to create database and API containers (you can open two tabs):

	docker-compose up db
	docker-compose up api

You can list running containers by running:

	docker ps

You can update fire data by running:

	docker exec -it $CONTAINER_ID /venv/bin/python3 update-fires.py

You can use the API directly throught the browser by going to `http://API_HOST:API_PORT/docs`.

## Structure documentation

Users interact with the frontend website and call this API, which uses a PostgreSQL database to store data. API and DB are isolated using Docker containers, which are like lightweight virtual machines.

Configuration variables used by `docker-compose` are in `.env`. If any configuration variable is changed, all affected containers should be ran again.

`JWT_SECRET_KEY` can be generated with OpenSSL:

	openssl rand -hex 32

`Dockerfile` contains the commands needed in order to create API Docker images. Python packages required by the API are listed in `requirements.txt`.

Configuration variables and cached files should be added to `.gitignore` so they are not tracked:

	.env
	__pycache__/

