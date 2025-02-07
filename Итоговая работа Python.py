import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()
# 1 и 2 аргумент - позиция окна (0,0 в левом верхнем углу),
# 3 и 4 аргумент - ширина и высота окна
window.setGeometry(400, 200, 500, 400)
window.setWindowTitle('Кто ты из Винни-Пуха?')
window.setWindowIcon(QIcon("icon.jpg"))
layout = QGridLayout()
window.setLayout(layout)

# Добавляет кнопку старта. Добавить действие - переход к тесту!
# Добавить кнопку в layout посередине! Разобраться с layout
#(текущие проблемы с выводом из-за того, что не все лежит в layout)
start_button = QPushButton("Начать!", window)
start_button.setGeometry(200, 300, 120, 40)

# Добавляет кнопки на верхнюю панель
toolbar = QToolBar()
layout.addWidget(toolbar,0,0)
test_toolbutton = QToolButton()
test_toolbutton.setText("Тест")
editor_toolbutton = QToolButton()
editor_toolbutton.setText("Редактирование")
# сюда вставить функции кнопок: Тест активная,
# Редактирование выводит экран с надписью:
# "Редактирование недоступно, сначала пройдите тест"
toolbar.addWidget(test_toolbutton)
toolbar.addWidget(editor_toolbutton)

window.show()


sys.exit(app.exec_())
