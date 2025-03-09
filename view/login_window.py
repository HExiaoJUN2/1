# view/login_window.py
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from controller.auth import login
from view.main_window import MainWindow  # 导入主界面类

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("登录系统")
        self.username_label = QLabel("用户名：")
        self.username_input = QLineEdit()
        self.password_label = QLabel("密码：")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("登录")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 绑定登录按钮事件
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user = login(username, password)
        if user:
            QMessageBox.information(self, "提示", "登录成功")
            # 关闭登录窗口，打开主界面
            self.main_window = MainWindow(username=user.username)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "警告", "用户名或密码错误")
