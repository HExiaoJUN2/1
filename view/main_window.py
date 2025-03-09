# view/main_window.py

from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QAction
from .archive_window import ArchiveWindow

class MainWindow(QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        self.setWindowTitle("档案管理系统 - 主界面")

        # 菜单栏
        menubar = self.menuBar()
        archive_menu = menubar.addMenu("档案")

        open_archive_window_action = QAction("打开档案管理", self)
        open_archive_window_action.triggered.connect(self.open_archive_window)
        archive_menu.addAction(open_archive_window_action)

        # 中心内容
        welcome_label = QLabel(f"欢迎, {self.username}!", self)
        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_archive_window(self):
        self.archive_window = ArchiveWindow()
        self.archive_window.show()
