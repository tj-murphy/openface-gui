from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

import sys  # For access to command line arguments


# Subclass QMainWindow for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()      # Must always call super to allow Qt to set up object in a subclass

        self.setWindowTitle("My Window")

        self.is_button_checked = True

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.fn_button_released)
        self.button.setChecked(self.is_button_checked)

        self.setFixedSize(QSize(400, 300)) 
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))

        self.setCentralWidget(self.button)   # Central widget
    
    
    # Get widget state when it changes
    def fn_button_released(self):
        self.is_button_checked = self.button.isChecked()
        print(self.is_button_checked)



# Only need one QApplication instance per application
# sys.argv allows for command line arguments
app = QApplication(sys.argv)

window = MainWindow()  # The window
window.show()   # Hidden by default

# Start event loop
app.exec()

# The lines after app.exec() will not be reached until the event loop has stopped (exit)