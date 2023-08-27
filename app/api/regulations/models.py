from sqlalchemy import Column, Integer, String, Text
from user_management.db.base_class import Base


class Regulation(Base):
    id = Column(Integer, primary_key=True)
    article_id = Column(String(50))
    content = Column(Text)
    title = Column(String(200))
