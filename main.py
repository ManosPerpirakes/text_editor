from PyQt6.QtWidgets import QApplication, QListWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFileDialog, QLineEdit
from os import listdir, path, remove
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer

def loadfolder():
    global workdir
    global files
    try:
        workdir = QFileDialog.getExistingDirectory()
        files = filter(listdir(workdir), '.txt')
        file_list.clear()
        for i in files:
            file_list.addItem(i)
    except:
        pass

def filter(files, extention):
    results = []
    for i in files:
        if i.endswith(extention):
            results.append(i)
    return results

def loadfile():
    try:
        global filepath
        filepath = path.join(workdir, files[file_list.currentRow()])
        with open(filepath, 'r') as file:
            display.setText(str(file.read()))
    except:
        print("could not read file")

def delete():
    global workdir
    global files
    try:
        remove(filepath)
        files = filter(listdir(workdir), '.txt')
        file_list.clear()
        for i in files:
            file_list.addItem(i)
        display.setText('')
    except:
        pass

def save():
    try:
        text = display.toPlainText()
        with open(filepath, 'w') as file:
            file.write(text)
    except:
        pass

def add():
    try:
        global filepath
        filepath = path.join(workdir, filename.text())
        filepath += '.txt'
        with open(filepath, 'w') as file:
            file.write(display.toPlainText())
        file_list.addItem((filename.text() + '.txt'))
        files.append((filename.text() + '.txt'))
        filename.clear()
    except:
        pass

def refresh():
    try:
        display.setFont(QFont('Arial', int(fontsizeinput.text())))
    except:
        pass

app = QApplication([])
w = QWidget()
w.setWindowTitle("Text editor")
w.resize(700, 500)
fontsizenum = 12
display = QTextEdit()
display.setFont(QFont('Arial', 15))
pb1 = QPushButton("load folder")
pb2 = QPushButton("delete")
pb3 = QPushButton("save")
pb4 = QPushButton('add')
file_list = QListWidget()
filename = QLineEdit()
filename.setPlaceholderText('enter file name:')
fontsizeinput = QLineEdit()
fontsizeinput.setPlaceholderText('enter font size:')
timer = QTimer()
l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()
l4 = QHBoxLayout()
l1.addWidget(pb1)
l1.addWidget(pb2)
l1.addWidget(pb3)
l1.addWidget(pb4)
l1.addWidget(filename)
l1.addWidget(fontsizeinput)
l2.addLayout(l1)
l3.addWidget(file_list)
l4.addWidget(display)
l4.addLayout(l3)
l2.addLayout(l4)
w.setLayout(l2)
w.show()
pb1.clicked.connect(loadfolder)
pb2.clicked.connect(delete)
pb3.clicked.connect(save)
pb4.clicked.connect(add)
file_list.currentRowChanged.connect(loadfile)
timer.timeout.connect(refresh)
timer.start(1000)
app.exec()