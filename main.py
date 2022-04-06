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

        JsonButton = QPushButton("Show raw json format")
        JsonButton.setFont(FontSmall)
        JsonButton.clicked.connect(self.JsonAnswer)

        EngineDropd = QComboBox(self)
        EngineDropd.addItem("google")
        EngineDropd.addItem("bing")
        EngineDropd.addItem("duckduckgo")
        EngineDropd.activated[str].connect(self.UpdateEngine)

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.QuestionLabel)
        HLayout.addWidget(self.input)
        HLayout.addWidget(self.colorCheckBox)
        HLayout.addWidget(EngineDropd)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(AskButton)
        VLayout.addWidget(JsonButton)
        VLayout.addWidget(self.TextEdit)

        Container = QWidget()
        Container.setMinimumSize(650, 480)
        Container.setLayout(VLayout)
        self.setCentralWidget(Container)

    def GetAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + self.engine + self.textColor))

    def JsonAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + self.engine + self.textColor + " -j"))

    def UpdateEngine(self, text):
        self.engine = " -e " + text
    
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