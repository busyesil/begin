import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QWidget, QVBoxLayout, QPushButton, QStackedWidget # type: ignore
from PyQt5.QtWidgets import QLineEdit


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subjective Testing Tool")
        centralWidget = QWidget()
      
        # Set the central/initial widget of the Window.
        self.setCentralWidget(centralWidget)
        mainLayout = QVBoxLayout(centralWidget)


        # Create a Stack widget to hold the different pages
        self.stack = QStackedWidget()
        mainLayout.addWidget(self.stack)

        #Create a widget for the initial layout
        initialWidget = QWidget()
        initialLayout = QVBoxLayout(initialWidget)

        # Initial layout/page
        self.mainTitle = QLabel("Subjective Testing Tool")
        self.dropDown = QComboBox()
        self.dropDown.addItems(["A/B Comparison Test", "Comparison Mean Opinion Score - 7 Point", "Live Listening Test", "Custom", "Saved Tests"])
        self.selectTest = QLabel("Please select which listening test you would like to conduct")
        self.doneButton = QPushButton("Done")
        #Button Press functionality
        self.doneButton.clicked.connect(self.doneButtonClicked)

        #Adding onto the initial layout
        initialLayout.addWidget(self.mainTitle)
        initialLayout.addWidget(self.selectTest)
        initialLayout.addWidget(self.dropDown)
        initialLayout.addWidget(self.doneButton)

        #Add the initial widget to the QStackedWidget
        self.stack.addWidget(initialWidget)

    # Open New Window based on listening test type
    def doneButtonClicked(self):
        selectedTest = self.dropDown.currentText()
        if self.dropDown.currentText() == "A/B Comparison Test":
            self.openAB()
        elif self.dropDown.currentText() == "Comparison Mean Opinion Score - 7 Point":
            self.openCMOS()
        elif self.dropDown.currentText() == "Live Listening Test":
            self.openLive()
        elif self.dropDown.currentText() == "Custom":
            self.openCustom()
        elif self.dropDown.currentText() == "Saved Tests":
            self.openSaved()
        else:
            self.openEmptyWindow()

    #"Go Back" button is pressed        
    def goBack(self):
        self.stack.setCurrentIndex((self.stack.currentIndex() - 1) % self.stack.count())
        

    #Create a new page        
    def CreateWindow(self, title):
        window = QWidget()
        windowLayout = QVBoxLayout()
        window.setLayout(windowLayout)

        # Clear the layout before adding any widgets
        while windowLayout.count():
            item = windowLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        label = QLabel(title)
        lineEdit = QLineEdit()
        windowLayout.addWidget(label)
        windowLayout.addWidget(lineEdit)
        button = QPushButton("Done")
        button.clicked.connect(lambda: self.stack.setCurrentIndex((self.stack.currentIndex() + 1 ) % self.stack.count()))
        windowLayout.addWidget(button)
        self.stack.addWidget(window)



    # A/B COMPARISON TEST
    def openAB(self):
        window = QWidget()
        windowLayout = QVBoxLayout() 
        window.setLayout(windowLayout)

        #Clear the layout before adding any widgets
        while windowLayout.count():
            item = windowLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        #Add to stack
        self.stack.addWidget(window)
        self.stack.setCurrentIndex(self.stack.count() - 1)
        
        #Add widgets to windowLayout
        self.testInfo = QLabel("Test Details:\n Name: A/B Comparison Test\n Description: Presents listeners with anonymized audio samples and asks them to compare and evaluate samples based on specified criteria.\n Duration: 10 minutes\n Requirements: Headphones\n Dimensions: 16-bit, 44.1 kHz\n Purpose: Identifying perceptible differences between samples.")
        windowLayout.addWidget(self.testInfo)

        loadTemplateButton = QPushButton("Load Test Template")
        loadTemplateButton.clicked.connect(self.openEmptyWindow)
        windowLayout.addWidget(loadTemplateButton)

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.stack.setCurrentIndex((self.stack.currentIndex() - 1) % self.stack.count()))
        windowLayout.addWidget(backButton)

        # Add new widgets to QStackedWidget
        self.stack.addWidget(window)

        # Set the current index to show the new widget
        self.stack.setCurrentIndex(self.stack.count() - 1)



    # CMOS COMPARISON TEST
    def openCMOS(self):
        window = QWidget()
        windowLayout = QVBoxLayout() 
        window.setLayout(windowLayout)

        #Clear the layout before adding any widgets
        while windowLayout.count():
            item = windowLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        #Add to stack
        self.stack.addWidget(window)
        self.stack.setCurrentIndex(self.stack.count() - 1)
        
        #Add widgets to windowLayout
        self.testInfo = QLabel("Test Details:\n Name: Comparison Mean Opinion Score - 7 Point\n Description: Presents listeners with anonymized audio samples and asks them to compare and evaluate samples based on specified criteria.\n Duration: 10 minutes\n Requirements: Headphones\n Dimensions: 16-bit, 44.1 kHz\n Purpose: Identifying perceptible differences between samples.")
        windowLayout.addWidget(self.testInfo)

        loadTemplateButton = QPushButton("Load Test Template")
        loadTemplateButton.clicked.connect(self.openEmptyWindow)
        windowLayout.addWidget(loadTemplateButton)

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.stack.setCurrentIndex((self.stack.currentIndex() - 1) % self.stack.count()))
        windowLayout.addWidget(backButton)

        # Add new widgets to QStackedWidget
        self.stack.addWidget(window)

        # Set the current index to show the new widget
        self.stack.setCurrentIndex(self.stack.count() - 1)


    # Opening a new window
    def openEmptyWindow(self):
        emptyWindow = QWidget()
        emptyWindowLayout = QVBoxLayout()
        emptyWindow.setLayout(emptyWindowLayout)

        #Clear the layout before adding any widgets
        while emptyWindowLayout.count():
            item = emptyWindowLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.stack.addWidget(emptyWindow)
        self.stack.setCurrentIndex(self.stack.count() - 1)

        



# LIVE COMPARISON TEST
    def openLive(self):
        pass



# CUSTOM TEST 
    def openCustom(self):
        pass


# SAVED TESTS
    def openSaved(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





