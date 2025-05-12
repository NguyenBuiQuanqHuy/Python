import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QIcon
from PIL import Image
import os

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()

        self.open_button = QPushButton("Open Image")
        self.open_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")
        self.open_button.clicked.connect(self.open_image)
        button_layout.addWidget(self.open_button)

        self.close_button = QPushButton("Close")
        self.close_button.setStyleSheet("background-color: #f44336; color: white; font-size: 16px;")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.close_button)

        main_layout.addLayout(button_layout)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.image_label)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("font-size: 14px; color: #333;")
        main_layout.addWidget(self.info_label)

        self.setLayout(main_layout)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg *.gif)")

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(600, 400, Qt.KeepAspectRatio))

            self.display_image_info(file_name)

    def display_image_info(self, file_name):
        try:
            img = Image.open(file_name)
            width, height = img.size
            creation_time = os.path.getctime(file_name)
            file_format = img.format

            info_text = f"Resolution: {width}x{height}\n"
            info_text += f"Format: {file_format}\n"
            info_text += f"Created on: {self.format_creation_time(creation_time)}"
            self.info_label.setText(info_text)
        except Exception as e:
            self.info_label.setText(f"Error: {str(e)}")

    def format_creation_time(self, timestamp):
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
