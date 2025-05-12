import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.height_label = QLabel('Chiều cao (m):', self)
        self.height_input = QLineEdit(self)

        self.weight_label = QLabel('Cân nặng (kg):', self)
        self.weight_input = QLineEdit(self)

        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_bmi)

        self.result_label = QLabel('', self)

        layout = QVBoxLayout()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('BMI Calculator')
        self.setFixedSize(300, 250)
        self.show()

    def calculate_bmi(self):
        try:
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())

            if height <= 0 or weight <= 0:
                self.result_label.setText('Chiều cao và cân nặng phải > 0.')
                return

            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            if bmi < 18.5:
                category = "Gầy"
            elif 18.5 <= bmi < 24.9:
                category = "Bình thường"
            elif 25 <= bmi < 29.9:
                category = "Thừa cân"
            else:
                category = "Béo phì"

            self.result_label.setText(f"BMI: {bmi} - {category}")

        except ValueError:
            self.result_label.setText('Vui lòng nhập số hợp lệ.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMICalculator()
    sys.exit(app.exec_())
