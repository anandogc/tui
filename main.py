import re
import sys
import typing
import inspect
import docutils.core

from dataclasses import fields

from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import  QFormLayout, QLabel, QWidget, QSpinBox, QDoubleSpinBox, QCheckBox
# from PyQt5.QtWebEngineWidgets import QWebView
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from TarangGUI import *
from config.FLUID_INCOMPRESS import Forces

class MyForm(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
#    self.ui.help_dropdown.activated.connect(self.disp_help)
    # self.ui.force_list_frame.hide()
    # self.ui.input_list_frame.hide()
    self.ui.actionSave.triggered.connect(self.save)
    self.ui.listWidget_3.itemDoubleClicked.connect(self.Add_force)
    
    reg = re.compile("Forces.(.*)'")

    for c in self.Get_list_of_classes(Forces):
        self.ui.listWidget_3.addItem(reg.findall(str(c))[0])

    # self.ui.listWidget_3.itemClicked.connect(self.Add_force)
    self.ui.move_Force_down_pushButton_2.clicked.connect(self.Add_force)
    self.ui.remove_force.clicked.connect(self.Remove_force)

    self.ui.move_up_Force_pushButton.clicked.connect(self.Move_up_force)
    self.ui.move_Force_down_pushButton.clicked.connect(self.Move_down_force)
    # for x in range(3):
    #   for y in range(3):
    #       hbox = QHBoxLayout()
    #       hbox.setSpacing(0)
    #       hbox.addWidget(QPushButton(str("Carati Scheme")))
    #       hbox.addWidget(QPushButton(str("x")))
    #       self.ui.forces_gridLayout.addLayout(hbox, x, y, alignment=Qt.AlignTop)

    # self.print_classes()

  def Add_force(self):
    self.ui.listWidget.addItem(self.ui.listWidget_3.currentItem().text())
    w = QWidget()
    form = QFormLayout()
    form.setWidget(0, QFormLayout.LabelRole, QLabel("Force: "))
    form.setWidget(0, QFormLayout.FieldRole, QLabel(self.ui.listWidget_3.currentItem().text()))
    w.setLayout(form)
    index = self.ui.stackedWidget.insertWidget(1000, w)
    self.ui.stackedWidget.setCurrentIndex(index)
    l = self.Get_list_of_classes(Forces)
    c = l[self.ui.listWidget_3.currentRow()]

    schema = c.__pydantic_model__.schema()
    properties = schema['properties']

    print(schema)
    i = 2
    for f in properties:
      print(f)
      form.setWidget(i, QFormLayout.LabelRole, QLabel(f))
      if properties[f]['type'] == 'integer':
        form.setWidget(i, QFormLayout.FieldRole, QSpinBox())
      if properties[f]['type'] == 'number':
        form.setWidget(i, QFormLayout.FieldRole, QDoubleSpinBox())
      if properties[f]['type'] == 'boolean':
        form.setWidget(i, QFormLayout.FieldRole, QCheckBox(""))
        # print(f + " is int")
      i += 2

  def Remove_force(self):
    self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

  def Move_up_force(self):
    row = self.ui.listWidget.currentRow()

    if row>=1:
      item = self.ui.listWidget.takeItem(row)
      self.ui.listWidget.insertItem(row-1, item.text())
      self.ui.listWidget.setCurrentRow(row-1)

  def Move_down_force(self):
    row = self.ui.listWidget.currentRow()
    count = self.ui.listWidget_3.count()

    if row>=0 and row<count-1:
      item = self.ui.listWidget.takeItem(row)
      self.ui.listWidget.insertItem(row+1, item.text())
      self.ui.listWidget.setCurrentRow(row+1)

  def Get_list_of_classes(self, module):
    l = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            l.append(obj)

    return l

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

  docutils.core.publish_file(
    source_path ="config/FLUID_INCOMPRESS/program.rst",
    destination_path ="Output.html",
    writer_name ="html")

  app = QApplication(sys.argv)
  w = MyForm()
  w.show()
  sys.exit(app.exec_())
