import sys
import qdarkstyle
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTextEdit, QComboBox, QCheckBox)
from PySide2.QtGui import QFont
from howdoi import howdoi
import global_tuning as tuning

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.engine = tuning.DEFAULT_SEARCH_ENGINE
        self.textColor = ""
        self.maxAnswers = "1"
        self.setWindowTitle("HowDoI - GUI")


        Font = QFont('Arial', tuning.STYLE_FONT_DIM, QFont.Bold)
        FontSmall = QFont('Arial', tuning.STYLE_FONT_SM_DIM, QFont.Bold)
        self.setFont(Font)

        self.input = QLineEdit()
        self.input.setFont(Font)
        self.QuestionLabel = QLabel()
        self.QuestionLabel.setFont(Font)
        self.QuestionLabel.setText("How do I:")

        self.TextEdit = QTextEdit()
        self.TextEdit.setFont(Font)
        self.TextEdit.setStyleSheet(f"border: {tuning.STYLE_BORDER}")
        self.TextEdit.setStyleSheet(f"background-color: {tuning.STYLE_BACKGROUND_COLOR}")

        self.colorCheckBox = QCheckBox("Text color", self)
        self.colorCheckBox.stateChanged.connect(self.TextColor)

        AskButton = QPushButton("Search")
        AskButton.setFont(Font)
        AskButton.clicked.connect(self.GetAnswer)

        MultiAskButton = QPushButton("Multiple search")
        MultiAskButton.setFont(Font)
        MultiAskButton.clicked.connect(self.GetMultipleAnswer)

        MaxAnswers = QComboBox(self)
        MaxAnswers.size()
        MaxAnswers.addItems("123456789")
        MaxAnswers.activated[str].connect(self.UpdateMaxAnswers)

        JsonButton = QPushButton("Show raw json format")
        JsonButton.setFont(FontSmall)
        JsonButton.clicked.connect(self.JsonAnswer)

        EngineDropd = QComboBox(self)
        EngineDropd.addItem("google")
        EngineDropd.addItem("bing")
        EngineDropd.addItem("duckduckgo")
        EngineDropd.activated[str].connect(self.UpdateEngine)

        MainInputLayout = QHBoxLayout()
        MainInputLayout.addWidget(self.QuestionLabel)
        MainInputLayout.addWidget(self.input)
        MainInputLayout.addWidget(self.colorCheckBox)
        MainInputLayout.addWidget(EngineDropd)

        MultiAnswerLayout = QHBoxLayout()
        MultiAnswerLayout.addWidget(MultiAskButton)
        MultiAnswerLayout.addWidget(MaxAnswers)

        WindowLayout = QVBoxLayout()
        WindowLayout.addLayout(MainInputLayout)
        WindowLayout.addWidget(AskButton)
        WindowLayout.addLayout(MultiAnswerLayout)
        WindowLayout.addWidget(JsonButton)
        WindowLayout.addWidget(self.TextEdit)

        Container = QWidget()
        Container.setMinimumSize(640, 480)
        Container.setLayout(WindowLayout)
        self.setCentralWidget(Container)

    def GetAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + self.engine + self.textColor))

    def GetMultipleAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + self.engine + self.textColor + " -n " + self.maxAnswers))

    def JsonAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + self.engine + self.textColor + " -j"))

    def UpdateEngine(self, text):
        self.engine = " -e " + text
    
    def UpdateMaxAnswers(self, text):
        self.maxAnswers = text
    
    def TextColor(self):
        if self.colorCheckBox.isChecked():
            self.textColor = " -c"
        else:
            self.textColor = ""


       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2()) # usign dark mode stylesheet
    window = MainWindow()
    window.show()

    app.exec_()