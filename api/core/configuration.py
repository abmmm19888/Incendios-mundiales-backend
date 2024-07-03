#!/user/bin/env python3

from os import getenv

JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
JWT_EXPIRE_TIME = int(getenv('JWT_EXPIRE_TIME'))
JWT_ALGORITHM = getenv('JWT_ALGORITHM')

if JWT_SECRET_KEY == None or JWT_EXPIRE_TIME == None or JWT_ALGORITHM == None:
    raise Exception("Authentication configuration not found")

FRONTEND_HOST = getenv('FRONTEND_HOST')
FRONTEND_PORT = getenv('FRONTEND_PORT')

if FRONTEND_HOST == None or FRONTEND_PORT == None:
    raise Exception("Frontend configuration not found")

DB_USER = getenv('POSTGRES_USER')
DB_PASSWORD = getenv('POSTGRES_PASSWORD')
DB_NAME = getenv('POSTGRES_DB')
DB_HOST = getenv('POSTGRES_HOST')
DB_PORT = getenv('PGPORT')

print(DB_USER, DB_PASSWORD)

if DB_USER == None or DB_PASSWORD == None or DB_HOST == None or DB_NAME == None or DB_PORT == None:
    raise Exception("Database configuration not found")

SQL_DATABASE_URL = "postgresql+psycopg2://%s:%s@%s:%s/%s" %(
	DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
