import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from TarangGUI import *

class MyForm(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.help_dropdown.activated.connect(self.disp_help)
		print("MyForm")

	def disp_help(self):
		print(self.ui.help_dropdown.currentIndex())
		self.ui.help.currentIndex = self.ui.help_dropdown.currentIndex()


if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())