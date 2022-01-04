import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from TarangGUI import *

class MyForm(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.help_dropdown.activated.connect(self.disp_help)
    self.ui.actionSave.triggered.connect(self.save)

  def disp_help(self):
    self.ui.help.setCurrentIndex(self.ui.help_dropdown.currentIndex())

  def save(self):
    print(rf"""
{{
   "program": {{
      "kind": "{self.ui.program_kind.currentText()}"
      "basis_type": "{self.ui.program_basis_type.currentText()}"
   }}

}}
      """)
      


if __name__=="__main__":
  app = QApplication(sys.argv)
  w = MyForm()
  w.show()
  sys.exit(app.exec_())