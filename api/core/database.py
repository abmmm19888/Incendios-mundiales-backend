#!/usr/bin/env python3

from os import getenv

DB_USER = getenv('POSTGRES_USER')
DB_PASSWORD = getenv('POSTGRES_PASSWORD')
DB_NAME = getenv('POSTGRES_DB')
DB_HOST = getenv('POSTGRES_HOST')
DB_PORT = getenv('PGPORT')

if DB_USER == None or DB_PASSWORD == None or DB_HOST == None or DB_NAME == None or DB_PORT == None:
    raise Exception("Database configuration not found")

SQL_DATABASE_URL = "postgresql+psycopg2://%s:%s@%s:%s/%s" %(
	DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(SQL_DATABASE_URL)
Session = sessionmaker(
	autocommit = False,
	autoflush = False,
	bind = engine
)

# Session is yielded so it is automatically closed.
def get_session():
	session = Session()
	
	try:
		yield session
	finally:
		session.close()
