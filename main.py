from PyQt6.QtWidgets import QApplication, QListWidget, QTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFileDialog, QLineEdit
from os import listdir, path, remove

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
        text = files[file_list.currentRow()]
        filepath = path.join(workdir, text)
        with open(filepath, 'r') as file:
            display.setText(str(file.read()))
    except:
        pass

def delete():
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
    except:
        pass

app = QApplication([])
w = QWidget()
w.setWindowTitle("Text editor")
w.resize(700, 500)
display = QTextEdit()
pb1 = QPushButton("load folder")
pb2 = QPushButton("delete")
pb3 = QPushButton("save")
pb4 = QPushButton('add')
file_list = QListWidget()
filename = QLineEdit()
filename.setPlaceholderText('enter file name:')
l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()
l4 = QHBoxLayout()
l1.addWidget(pb1)
l1.addWidget(pb2)
l1.addWidget(pb3)
l1.addWidget(pb4)
l1.addWidget(filename)
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
app.exec()