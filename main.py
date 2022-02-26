import re
import sys
import typing
import inspect

from dataclasses import fields

from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QFormLayout, QLabel, QWidget, QSpinBox, QDoubleSpinBox
from PyQt5.QtWidgets import QCheckBox, QListWidgetItem, QTextEdit
# from PyQt5.QtWebEngineWidgets import QWebView
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from TarangGUI import *
from config.FLUID_INCOMPRESS import Input
from config.FLUID_INCOMPRESS import Forces
from config.FLUID_INCOMPRESS import Output

class MyForm(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
#    self.ui.help_dropdown.activated.connect(self.disp_help)
    # self.ui.force_list_frame.hide()
    # self.ui.input_list_frame.hide()
    self.ui.actionSave.triggered.connect(self.save)
    self.ui.listWidget_4.itemDoubleClicked.connect(self.Add_force)
    # self.ui.comboBox_2.activated.connect(self.Add_output)

    self.Add_input()

    reg = re.compile("Forces.(.*)'")

    i = 0
    for c in self.Get_list_of_classes(Forces):
        name = reg.findall(str(c))[0]
        name = name.replace("_", " ")
        name = name.capitalize()
        item = QListWidgetItem(name)
        item.setData(1, i)
        self.ui.listWidget_4.addItem(item)
        i = i + 1

    """
    reg = re.compile("Output.(.*)'")

    i = 0
    for c in self.Get_list_of_classes(Output):
        name = reg.findall(str(c))[0]
        name = name.replace("_", " ")
        name = name.capitalize()
        # item = QListWidgetItem(name)
        # item.setData(1, i)
        self.ui.comboBox_2.addItem(name)
        i = i + 1
    """
    # self.ui.comboBox_2.sortItems()

    # self.ui.listWidget_4.itemClicked.connect(self.Add_force)
    self.ui.add_Force_pushButton.clicked.connect(self.Add_force)
    self.ui.remove_Force_pushButton.clicked.connect(self.Remove_force)
    #self.ui.pushButton.clicked.connect(self.Remove_output)

    # self.ui.move_up_Force_pushButton.clicked.connect(self.Move_up_force)
    # self.ui.move_Force_down_pushButton.clicked.connect(self.Move_down_force)
    # for x in range(3):
    #   for y in range(3):
    #       hbox = QHBoxLayout()
    #       hbox.setSpacing(0)
    #       hbox.addWidget(QPushButton(str("Carati Scheme")))
    #       hbox.addWidget(QPushButton(str("x")))
    #       self.ui.forces_gridLayout.addLayout(hbox, x, y, alignment=Qt.AlignTop)

    # self.print_classes()

  def Add_input(self):
    reg = re.compile("Input.(.*)'")

    for c in self.Get_list_of_classes(Input):
        name = reg.findall(str(c))[0]
        name = name.replace("_", " ")
        name = name.capitalize()
        # item = QListWidgetItem(name)
        # item.setData(1, i)
        self.ui.Input_list.addItem(name)

        w = QWidget()
        form = QFormLayout()
        form.setWidget(0, QFormLayout.LabelRole, QLabel("Input: "))
        form.setWidget(0, QFormLayout.FieldRole, QLabel(name))
        w.setLayout(form)

        schema = c.__pydantic_model__.schema()
        properties = schema['properties']

        i = 2
        for f in properties:
          form.setWidget(i, QFormLayout.LabelRole, QLabel(f))
          if properties[f]['type'] == 'integer':
            form.setWidget(i, QFormLayout.FieldRole, QSpinBox())
          if properties[f]['type'] == 'number':
            form.setWidget(i, QFormLayout.FieldRole, QDoubleSpinBox())
          if properties[f]['type'] == 'boolean':
            form.setWidget(i, QFormLayout.FieldRole, QCheckBox(""))
          i += 2

        index = self.ui.stackedWidget_2.insertWidget(1000, w)

        h = QTextEdit()
        h.setPlainText(c.__doc__)
        self.ui.stackedWidget_6.insertWidget(1000, h)

  def Add_force(self):
    F = self.Get_list_of_classes(Forces)[self.ui.listWidget_4.currentRow()]

    item = self.ui.listWidget_4.takeItem(self.ui.listWidget_4.currentRow())
    # item.setData(0, self.ui.listWidget_4.currentIndex())
    self.ui.listWidget_5.addItem(item)
    self.ui.listWidget_5.setCurrentRow(self.ui.listWidget_5.count()-1)
    w = QWidget()
    form = QFormLayout()
    form.setWidget(0, QFormLayout.LabelRole, QLabel("Force: "))
    form.setWidget(0, QFormLayout.FieldRole, QLabel(item.text()))
    w.setLayout(form)
    index = self.ui.stackedWidget_4.insertWidget(1000, w)
    self.ui.stackedWidget_4.setCurrentIndex(index)

    F = self.Get_list_of_classes(Forces)[self.ui.listWidget_4.currentRow()]
    text = QTextEdit()
    text.setPlainText(F.__doc__)
    index = self.ui.stackedWidget_5.insertWidget(1000, text)
    self.ui.stackedWidget_5.setCurrentIndex(index)

    schema = F.__pydantic_model__.schema()
    properties = schema['properties']

    i = 2
    for f in properties:
      form.setWidget(i, QFormLayout.LabelRole, QLabel(f))
      if properties[f]['type'] == 'integer':
        form.setWidget(i, QFormLayout.FieldRole, QSpinBox())
      if properties[f]['type'] == 'number':
        form.setWidget(i, QFormLayout.FieldRole, QDoubleSpinBox())
      if properties[f]['type'] == 'boolean':
        form.setWidget(i, QFormLayout.FieldRole, QCheckBox(""))
      i += 2

  def Remove_force(self):
    item = self.ui.listWidget_5.takeItem(self.ui.listWidget_5.currentRow())
    self.ui.listWidget_4.addItem(item)
    self.ui.listWidget_4.sortItems()

  def Add_output(self):
    item = self.ui.comboBox_2.currentText()
    # item.setData(0, self.ui.listWidget_4.currentIndex())
    self.ui.listWidget.addItem(item)
    w = QWidget()
    form = QFormLayout()
    form.setWidget(0, QFormLayout.LabelRole, QLabel("Module: "))
    form.setWidget(0, QFormLayout.FieldRole, QLabel(item))
    w.setLayout(form)
    index = self.ui.stackedWidget.insertWidget(1000, w)
    self.ui.stackedWidget.setCurrentIndex(index)
    l = self.Get_list_of_classes(Output)
    c = l[self.ui.comboBox_2.currentIndex()]

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

  def Remove_output(self):
    # print(self.ui.stackedWidget.currentIndex())
    self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(self.ui.listWidget.currentRow()))
    item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    # self.ui.comboBox_2.addItem(item)
    # self.ui.comboBox_2.sortItems()


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
  app = QApplication(sys.argv)
  w = MyForm()
  w.show()
  sys.exit(app.exec_())
