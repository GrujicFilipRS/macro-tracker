from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..db.db_session import SqlAlchemyBase


class Eaten(SqlAlchemyBase):
    __tablename__ = 'eaten'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    food_name = Column(String, nullable=False)
    datetime_eaten = Column(DateTime, nullable=False)
    num_proteins = Column(Integer, nullable=False)
    num_carbs = Column(Integer, nullable=False)
    num_fats = Column(Integer, nullable=False)

    user = relationship('User', back_populates='eaten_items')

    def to_dict(self) -> dict:
        data: dict = {
            'id': self.id,
            'user_id': self.user_id,
            'food_item': self.food_item,
            'datetime_eaten': self.datetime_eaten,
            'num_proteins': self.num_proteins,
            'num_carbs': self.num_carbs,
            'num_fats': self.num_fats,
            }

        return data