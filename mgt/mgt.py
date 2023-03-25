#!/home/jamessmithies/Apps/anaconda3/bin/python python3

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PyQt6.QtCore import QProcess, QSize
import sys
import re
import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None

        self.setWindowTitle("Management Console")
        self.setFixedSize(QSize(400, 600))

        self.btn = QPushButton("Save Static Files")
        self.btn.pressed.connect(self.start_static_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.btn2 = QPushButton("Publish Latest Static Files")
        self.btn2.pressed.connect(self.start_git_process)
        self.text2 = QPlainTextEdit()
        self.text2.setReadOnly(True)

        self.btn3 = QPushButton("Publish Latest Mastodon")
        self.btn3.pressed.connect(self.start_mastodon_process)
        self.text3 = QPlainTextEdit()
        self.text3.setReadOnly(True)

        self.btn4 = QPushButton("Back up Fixtures")
        self.btn4.pressed.connect(self.start_backup_process)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.btn2)
        l.addWidget(self.btn3)
        l.addWidget(self.btn4)
        l.addWidget(self.text)
        l.addWidget(self.text2)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def message2(self, s):
        self.text2.appendPlainText(s)
    
    def start_static_process(self):
        if self.p is None:  # No process running.
            self.message("Saving website...")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("bash", ['/Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/mgt/qtmakestatic.sh'])
   
    def start_backup_process(self):
        if self.p is None:  # No process running.
            self.message("Backing up...")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("bash", ['/Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/mgt/qtbackup.sh'])

    def start_mastodon_process(self):
        if self.p is None:  # No process running.
            self.message("Publishing...")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("bash", ['/Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/mgt/git_mastodon.sh'])

    def start_git_process(self):
        if self.p is None:  # No process running.
            self.message2("Publishing...")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("bash", ['/Users/jamessmithies/Library/CloudStorage/Dropbox/Technical/dev/jamessmithies.org/mgt/git_publish.sh'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message2(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message2(stdout)

    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: 'Not running',
            QProcess.ProcessState.Starting: 'Starting',
            QProcess.ProcessState.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None
    
    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: 'Not running',
            QProcess.ProcessState.Starting: 'Starting',
            QProcess.ProcessState.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None

app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()