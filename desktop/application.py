#!/bin/env python

from config import settings

import sys, signal
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class Application(QApplication):

	def __init__(self,argv,style='Fusion'):
		super(Application, self).__init__(argv)
		self.setStyle(style)
		self.initPalette()

	def initPalette(self):
		palette = QPalette()
		palette.setColor(QPalette.Window, QColor(53,53,53))
		palette.setColor(QPalette.WindowText, Qt.white)
		palette.setColor(QPalette.Base, QColor(15,15,15))
		palette.setColor(QPalette.AlternateBase, QColor(53,53,53))
		palette.setColor(QPalette.ToolTipBase, Qt.white)
		palette.setColor(QPalette.ToolTipText, Qt.white)
		palette.setColor(QPalette.Text, Qt.white)
		palette.setColor(QPalette.Button, QColor(53,53,53))
		palette.setColor(QPalette.ButtonText, Qt.white)
		palette.setColor(QPalette.BrightText, Qt.red)

		palette.setColor(QPalette.Highlight, QColor(142,45,197).lighter())
		palette.setColor(QPalette.HighlightedText, Qt.black)
		self.setPalette(palette)

class UI(QWidget):

	def __init__(self,title="Window Title"):
		super(UI, self).__init__()

		layout = QVBoxLayout()
		label = QLabel("Test")

		layout.addWidget(label)
		self.setLayout(layout)

		self.setWindowTitle(title)

		self.show()


if __name__ == "__main__":

	# close app and window using CRTL + C
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	# initialize application
	app = Application(sys.argv,style=settings.style)

	# initialize widgets
	ex = UI(title=settings.title)

	# run app
	app.exec_()

