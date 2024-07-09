import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QWidget, QVBoxLayout


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subjective Testing Tool")
        centralWidget = QWidget()

    
        # Set the central widget of the Window.
        self.setCentralWidget(centralWidget)
        self.layout = QVBoxLayout(centralWidget)

        # Declaring global variables
        self.mainTitle = QLabel("Subjective Testing Tool")
        self.dropDown = QComboBox()
        self.dropDown.addItems(["MUSHRA", "A/B Listening Test", "Live Listening Test", "Custom"])
        self.selectTest = QLabel("Please select which listening test you would like to conduct")
 
        #Adding onto the Central Widget
        self.layout.addWidget(self.mainTitle)
        self.layout.addWidget(self.selectTest)
        self.layout.addWidget(self.dropDown)
      
        
        

#Dropdown menu

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
