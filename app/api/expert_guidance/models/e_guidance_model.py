from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base


class ExpertGuidance(Base):
    id = Column(Integer, primary_key=True)
    query = Column(String(50))
    user_id = Column(Integer)
    result = Column(String(200))
    content = Column(Text)
