# main.py
import sys
from PyQt5.QtWidgets import QApplication
from model.db_init import init_db
from controller.auth import create_user
from view.login_window import LoginWindow

def main():
    # 初始化数据库
    init_db()

    # 创建测试用户，注意如果用户已存在会有提示
    create_user("alice", "123456")

    # 启动登录窗口
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
