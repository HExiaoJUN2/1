# view/archive_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from controller.archive_controller import get_all_archives, create_archive, delete_archive

class ArchiveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("档案管理")
        self.initUI()

    def initUI(self):
        # 主布局
        main_widget = QWidget()
        self.layout = QVBoxLayout()

        # 档案列表表格
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # 刷新按钮
        refresh_btn = QPushButton("刷新")
        refresh_btn.clicked.connect(self.load_archives)
        self.layout.addWidget(refresh_btn)

        # 创建档案按钮
        create_btn = QPushButton("新建档案")
        create_btn.clicked.connect(self.handle_create_archive)
        self.layout.addWidget(create_btn)

        # 删除档案按钮
        delete_btn = QPushButton("删除选中档案")
        delete_btn.clicked.connect(self.handle_delete_archive)
        self.layout.addWidget(delete_btn)

        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

        # 先加载一下档案列表
        self.load_archives()

    def load_archives(self):
        """
        从数据库查询所有档案，并在表格中显示
        """
        archives = get_all_archives()
        self.table.clear()
        self.table.setColumnCount(4)  # id, title, category, upload_time
        self.table.setHorizontalHeaderLabels(["ID", "标题", "类别", "上传时间"])
        self.table.setRowCount(len(archives))

        for row, archive in enumerate(archives):
            self.table.setItem(row, 0, QTableWidgetItem(str(archive.id)))
            self.table.setItem(row, 1, QTableWidgetItem(archive.title))
            self.table.setItem(row, 2, QTableWidgetItem(archive.category if archive.category else ""))
            self.table.setItem(row, 3, QTableWidgetItem(str(archive.upload_time)))

    def handle_create_archive(self):
        """
        简单示例：创建一个演示档案
        实际开发中你可以弹出对话框，让用户输入档案信息
        """
        create_archive("测试档案", "演示", file_path="C:/temp/demo.txt")
        self.load_archives()

    def handle_delete_archive(self):
        """
        获取表格选中行的ID并删除
        """
        row = self.table.currentRow()
        if row < 0:
            print("请先选中要删除的档案。")
            return
        archive_id = self.table.item(row, 0).text()
        delete_archive(archive_id)
        self.load_archives()
