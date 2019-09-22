# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FpgaTool
   Description :
   Author :       Rex
   date：          2019/9/20
-------------------------------------------------
   Change Activity:
                   2019/9/20:
-------------------------------------------------
"""
__author__ = 'Rex'

import sys
import os
import time
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_FpgaTool
import syntax_highlight
from genHdlInst import *


class FpgaTool(Ui_FpgaTool, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_FpgaTool.__init__(self)
        self.setupUi(self)



class ToolApp(FpgaTool):
    def __init__(self):
        FpgaTool.__init__(self)
        self.setWindowTitle('FPGA Tool')
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/fpga.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon2)

        self.actionNew_File.triggered.connect(lambda: self.on_newfile(''))
        self.actionOpen_File.triggered.connect(self.on_openfile)
        self.actionSave_File.triggered.connect(self.on_savefile)
        self.actionTiled.triggered.connect(self.on_tiled)
        self.actionCascade.triggered.connect(self.on_cascade)
        self.actionView_HDL_Inst.triggered.connect(self.on_viewInst)

        self.winCount = 0

    def on_newfile(self, text):
        self.winCount += 1
        sub = QMdiSubWindow()
        editor = QTextEdit()
        sub.setWidget(editor)
        highlight = syntax_highlight.PythonHighlighter(editor)
        editor.setPlainText(text)
        editor.setFont(QtGui.QFont("Timers", 14))
        self.mdi.addSubWindow(sub)
        sub.setWindowIcon(QIcon('./pic/text.png'))
        sub.setWindowTitle('New' + str(self.winCount))
        sub.showMaximized()

    def on_savefile(self):
        curSubWin = self.mdi.currentSubWindow()
        if curSubWin == None:
            return None

        if os.path.exists(curSubWin.windowTitle()):
            with open(curSubWin.windowTitle(),'w') as f:
                f.write(curSubWin.widget().toPlainText())
        else:
            try:
                fname,_ = QFileDialog.getSaveFileName(self, 'Save file', '.', 'text file (*.v *.txt)')
                print(fname)
                with open(fname[0],'w') as f:
                    f.write(curSubWin.widget().toPlainText())
                    curSubWin.setWindowTitle(fname)
            except:
                return None


    def on_openfile(self):
        try:
            fname,_ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'text file (*.v *.txt)')
            with open(fname, 'r') as f:
                cont = f.read()
                sub = QMdiSubWindow()
                editor = QTextEdit()
                sub.setWidget(editor)
                highlight = syntax_highlight.PythonHighlighter(editor)
                editor.setPlainText(cont)
                editor.setFont(QtGui.QFont("Timers" , 14))
                self.mdi.addSubWindow(sub)
                sub.setWindowIcon(QIcon('./pic/text.png'))
                sub.setWindowTitle(fname)
                sub.showMaximized()
        except:
            return None




    def on_cascade(self):
        # print('cascade')
        self.mdi.cascadeSubWindows()

    def on_tiled(self):
        # print('tiled')
        self.mdi.tileSubWindows()

    def on_viewInst(self):
        curSubWin = self.mdi.currentSubWindow()
        if curSubWin == None:
            return None

        text = curSubWin.widget().toPlainText()
        try:
            instTempl = genHdlInst(text)
            self.on_newfile(instTempl)
            self.on_tiled()
        except HdlError:
            print('error')
            self.critical_dlg()
            return None

        # print(rm_res)

    def critical_dlg(self):
        reply = QMessageBox.critical(self, "Error", "HDL Syntax error!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolApp()
    main.show()
    sys.exit(app.exec_())


