# model/user.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from controller.security import pwd_context

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def set_password(self, password: str):
        """
        使用 passlib/bcrypt 对明文密码进行哈希后存储
        """
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """
        验证输入的明文密码与存储的哈希是否匹配
        """
        return pwd_context.verify(password, self.password_hash)
