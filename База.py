from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.resize(200, 400)

txt = QLabel("TEXT ABOUT IQOS")
btn = QPushButton("BUTTON")
v_line = QVBoxLayout()
v_line.addWidget(txt, alignment=Qt.AlignCenter)
v_line.addWidget(btn)

main_win.setLayout(v_line)

def mykola():
    txt.setText("Mykola smokes IQOS")

btn.clicked.connect(mykola)

main_win.show()
app.exec_()