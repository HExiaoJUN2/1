# model/archive.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

Base = declarative_base()

class Archive(Base):
    __tablename__ = "archives"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)        # 档案标题
    category = Column(String(50))                     # 档案类别
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
    file_path = Column(String(255))                   # 文件存储路径（可选）

    def __repr__(self):
        return f"<Archive(title='{self.title}', category='{self.category}')>"
