# model/db_init.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base as UserBase
from model.archive import Base as ArchiveBase

engine = create_engine("sqlite:///mydatabase.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    # 注意：UserBase.metadata.create_all(bind=engine) 只会创建 user 表
    # 如果ArchiveBase和UserBase是同一个Base实例，可以直接写 Base.metadata
    # 如果不是，需要分别创建
    UserBase.metadata.create_all(bind=engine)
    ArchiveBase.metadata.create_all(bind=engine)
    print("数据库初始化完成！")
