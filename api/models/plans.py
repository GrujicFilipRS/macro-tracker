from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db.db_session import SqlAlchemyBase

class Plan(SqlAlchemyBase):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    num_proteins = Column(Integer, nullable=False)
    num_carbs = Column(Integer, nullable=False)
    num_fats = Column(Integer, nullable=False)

    owner = relationship('User', back_populates='plans')

    def to_dict(self, no_owner=False) -> dict:
        data: dict = {
            'id': self.id,
            'name': self.name,
            'num_proteins': self.num_proteins,
            'num_carbs': self.num_carbs,
            'num_fats': self.num_fats
        }

        if not no_owner:
            data['owner_id'] = self.owner_id

        return data