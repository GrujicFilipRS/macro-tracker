from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from ..db.db_session import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    plans = relationship('Plan', back_populates='owner')

    def to_dict(self) -> dict:
        data: dict = {
            'id': self.id,
            'username': self.username
        }

        return data

    def set_password(self, password: str) -> None:
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.hashed_password, password)
    
    @staticmethod
    def validate_username(username: str) -> bool:
        if username.lower() != username:
            return False
        
        ALLOWED_CHARS = set([c for c in 'abcdefghijklmnopqrstuvwxyz0123456789_'])

        if not all([char in ALLOWED_CHARS for char in username]):
            return False

        if len(username) < 7 or len(username) > 15:
            return False

        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        return len(password) > 7 and len(password) < 15