#!/user/bin/env python3

from core.configuration import SQL_DATABASE_URL
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
