#!/user/bin/env python3

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.models import User
from schemas.user import UserCreationData
from core.password import verify_password, hash_password
from services.token import TokenService
from jose import JWTError

class UserService:
	@staticmethod
	def create_user(data: UserCreationData, session: Session):
		user = User(
			username = data.username,
			hashed_password = hash_password(data.password),
			email = data.email)
		
		session.add(user)

		try:
			session.commit()
		except IntegrityError:
			return None
		
		session.refresh(user)
		return user
	
	@staticmethod
	def read_user_by_uuid(uuid: int, session: Session):
		user = session.query(User).get(uuid)
		return user
	
	@staticmethod
	def read_user_by_username(username: str, session: Session):
		user = session.query(User).filter_by(username = username).first()
		return user

	@staticmethod
	def read_user_by_credentials(username, password, session: Session):
		# FIXME
		user = session.query(User).filter_by(username = username).first()
		
		if not user:
			return False
		if not verify_password(password, user.hashed_password):
			return False
		
		return user

	@staticmethod
	def read_user_by_token(token: str, session: Session):
		try:
			username = TokenService.read_token_username(token)
		except JWTError:
			return None

		user = UserService.read_user_by_username(username, session)

		return user

	@staticmethod
	def update_user(session: Session):
		...
	
	@staticmethod
	def delete_user(session: Session):
		...

