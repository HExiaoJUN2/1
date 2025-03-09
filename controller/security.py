# controller/security.py
from passlib.context import CryptContext

# 创建一个哈希上下文，指定使用bcrypt算法
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
