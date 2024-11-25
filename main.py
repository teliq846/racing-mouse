from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon
import pyautogui
import threading
import sys
import keyboard  # 用于全局热键


class MouseClickTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.running = False
        self.delay = 100  # 默认间隔时间 100ms
        self.mouse_button = "left"
        self.wait_seconds = 3

        # 绑定 F1 热键
        self.setup_hotkey()

    def init_ui(self):
        self.setWindowTitle("MouseClickTool")
        self.setGeometry(100, 100, 400, 300)

        # 设置窗口图标
        self.setWindowIcon(QIcon("icons/app_icon.png"))  # 替换为您自己的图标路径

        # 创建主窗口部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 创建布局
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # 标题
        self.title_label = QLabel("🏎Racing Mouse🐀")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setStyleSheet("color: #4CAF50;")
        layout.addWidget(self.title_label)

        # 间隔时间标签和输入框
        self.interval_label = QLabel("Interval (ms):")
        self.interval_label.setStyleSheet("font-size: 14px; color: #333;")
        layout.addWidget(self.interval_label)

        self.interval_input = QLineEdit()
        self.interval_input.setText("100")  # 默认值
        self.interval_input.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.interval_input)

        # 鼠标按钮选择
        self.button_label = QLabel("Mouse Button:")
        self.button_label.setStyleSheet("font-size: 14px; color: #333;")
        layout.addWidget(self.button_label)

        self.button_selector = QComboBox()
        self.button_selector.addItems(["Left", "Right"])
        self.button_selector.setStyleSheet("""
            QComboBox {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.button_selector)

        # 启动/停止按钮
        self.start_button = QPushButton("Start")
        self.start_button.setIcon(QIcon("icons/start_icon.png"))  # 替换为您自己的图标路径
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.start_button.clicked.connect(self.toggle_clicking)
        layout.addWidget(self.start_button)

        # 提示信息
        self.info_label = QLabel("Press F1 to Start/Stop")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.info_label)

        # 设置布局
        self.central_widget.setLayout(layout)

    def setup_hotkey(self):
        # 添加 F1 热键绑定
        keyboard.add_hotkey("f1", self.toggle_clicking)

    def toggle_clicking(self):
        if self.running:
            self.running = False
            self.start_button.setText("Start")
            self.start_button.setIcon(QIcon("icons/start_icon.png"))  # 切换回启动图标
        else:
            try:
                self.delay = int(self.interval_input.text())
                self.mouse_button = "left" if self.button_selector.currentText() == "Left" else "right"
                self.running = True
                self.start_button.setText("Stop")
                self.start_button.setIcon(QIcon("icons/stop_icon.png"))  # 切换为停止图标
                threading.Thread(target=self.start_clicking, daemon=True).start()
            except ValueError:
                QMessageBox.critical(self, "Error", "Interval must be a valid number!")

    def start_clicking(self):
        timer = QTimer()
        timer.timeout.connect(self.update_button)
        timer.start(1000)
        threading.Event().wait(self.wait_seconds)
        while self.running:
            pyautogui.click(button=self.mouse_button)
            threading.Event().wait(self.delay / 1000)

    def update_button(self):
        if self.running:
            self.start_button.setText("Clicking...")

    def closeEvent(self, event):
        # 释放热键
        keyboard.unhook_all_hotkeys()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置全局样式表
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f9f9f9;
        }
    """)

    window = MouseClickTool()
    window.show()
    sys.exit(app.exec_())
