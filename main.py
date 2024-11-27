import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self, x, y, diameter, color):
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.drawing_area = DrawingArea()
        self.drawing_area.setStyleSheet("background-color: white;")
        self.layout.addWidget(self.drawing_area)

        self.add_circle_button = QPushButton("Добавить окружность")
        self.add_circle_button.clicked.connect(self.add_circle)
        self.layout.addWidget(self.add_circle_button)

    def add_circle(self):
        x = random.randint(0, self.drawing_area.width() - 50)
        y = random.randint(0, self.drawing_area.height() - 50)
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.drawing_area.add_circle(x, y, diameter, color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
