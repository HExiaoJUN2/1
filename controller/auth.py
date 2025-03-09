# controller/auth.py
from model.db_init import SessionLocal
from model.user import User

def create_user(username: str, password: str):
    """
    创建新用户，先检查用户名是否已存在，再哈希密码并保存
    """
    db = SessionLocal()
    try:
        # 检查是否已存在同名用户
        existing_user = db.query(User).filter_by(username=username).first()
        if existing_user:
            print(f"用户名 '{username}' 已存在，无法创建。")
            return

        # 创建用户并设置密码
        new_user = User(username=username)
        new_user.set_password(password)
        db.add(new_user)
        db.commit()
        print(f"用户 '{username}' 创建成功！")
    except Exception as e:
        db.rollback()
        print("创建用户时出错：", e)
    finally:
        db.close()

def login(username: str, password: str):
    """
    登录验证：从数据库查找用户，并验证密码是否正确
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            print("登录成功！")
            return user  # 返回 User 对象或 True 都可以
        else:
            print("用户名或密码错误！")
            return None
    except Exception as e:
        print("登录出错：", e)
        return None
    finally:
        db.close()
