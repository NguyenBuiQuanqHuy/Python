import sys
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPainter, QKeyEvent

class Tetris(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tetris Game")
        self.setGeometry(100, 100, 300, 600)
        self.setStyleSheet("background-color: black;")

        # Kích thước khối
        self.block_size = 30

        # Lưới game (10x20)
        self.board_width = 10
        self.board_height = 20
        self.board = [[0 for _ in range(self.board_width)] for _ in range(self.board_height)]

        # Hình dạng của các khối (S, Z, L, T, I, O)
        self.shapes = [
            [[1, 1, 1], [0, 1, 0]],  # T-shape
            [[1, 1], [1, 1]],        # O-shape
            [[0, 1, 1], [1, 1, 0]],  # S-shape
            [[1, 1, 0], [0, 1, 1]],  # Z-shape
            [[1, 0, 0], [1, 1, 1]],  # L-shape
            [[0, 0, 1], [1, 1, 1]],  # J-shape
            [[1, 1, 1, 1]]           # I-shape
        ]

        self.shape_colors = [Qt.cyan, Qt.yellow, Qt.green, Qt.red, Qt.blue, Qt.orange, Qt.magenta]

        self.current_shape = None
        self.current_position = [0, 0]

        # Timer để làm cho các khối di chuyển xuống
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_down)
        self.timer.start(500)  # 500ms

        self.spawn_shape()

    def spawn_shape(self):
        """Tạo ra một khối mới ngẫu nhiên"""
        shape_idx = random.randint(0, len(self.shapes) - 1)
        self.current_shape = self.shapes[shape_idx]
        self.current_color = self.shape_colors[shape_idx]
        self.current_position = [0, self.board_width // 2 - len(self.current_shape[0]) // 2]

    def rotate_shape(self):
        """Xoay khối hiện tại"""
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    def move_down(self):
        """Di chuyển khối xuống"""
        self.current_position[0] += 1
        if self.check_collision():
            self.current_position[0] -= 1
            self.place_shape()
            self.spawn_shape()
            if self.check_collision():
                self.game_over()
        self.update()

    def move_left(self):
        """Di chuyển khối sang trái"""
        self.current_position[1] -= 1
        if self.check_collision():
            self.current_position[1] += 1
        self.update()

    def move_right(self):
        """Di chuyển khối sang phải"""
        self.current_position[1] += 1
        if self.check_collision():
            self.current_position[1] -= 1
        self.update()

    def check_collision(self):
        """Kiểm tra xem khối có va chạm với các khối khác hoặc rìa bảng không"""
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = self.current_position[1] + x
                    board_y = self.current_position[0] + y
                    if board_x < 0 or board_x >= self.board_width or board_y >= self.board_height or self.board[board_y][board_x]:
                        return True
        return False

    def place_shape(self):
        """Đặt khối vào bảng và xóa các dòng đầy"""
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = self.current_position[1] + x
                    board_y = self.current_position[0] + y
                    self.board[board_y][board_x] = self.current_color
        self.clear_lines()

    def clear_lines(self):
        """Xóa các dòng đầy"""
        self.board = [row for row in self.board if any(cell == 0 for cell in row)]
        while len(self.board) < self.board_height:
            self.board.insert(0, [0] * self.board_width)

    def game_over(self):
        """Kết thúc game"""
        self.timer.stop()
        print("Game Over")
        self.close()

    def paintEvent(self, event):
        """Vẽ bảng và các khối"""
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        # Vẽ bảng
        for y in range(self.board_height):
            for x in range(self.board_width):
                color = self.board[y][x]
                if color:
                    painter.setBrush(color)
                    painter.drawRect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)

        # Vẽ khối hiện tại
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    painter.setBrush(self.current_color)
                    painter.drawRect((self.current_position[1] + x) * self.block_size,
                                     (self.current_position[0] + y) * self.block_size,
                                     self.block_size, self.block_size)

    def keyPressEvent(self, event: QKeyEvent):
        """Xử lý sự kiện khi nhấn phím"""
        if event.key() == Qt.Key_Left:
            self.move_left()
        elif event.key() == Qt.Key_Right:
            self.move_right()
        elif event.key() == Qt.Key_Up:
            self.rotate_shape()
        elif event.key() == Qt.Key_Down:
            self.move_down()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Tetris()
    game.show()
    sys.exit(app.exec_())
