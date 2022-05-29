#! /usr/bin/python3
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets


def time_date():
    t = time.strftime("%d/%m/%Y")
    return t


def check():
    """ Вытягивание значений из базы """
    with open('check.txt', "r") as a:
        cash_day = int(a.readline())
    return cash_day


def check_z(time_day):
    """ Ведение базы """
    with open('check.txt', "w") as a:
        print(time_day, file=a)


def archive(n, data, cash_day, cash_collation):
    with open('Ar.txt', "a") as ar:
        if n == 1:
            print(f"{data} Было изъято {cash_collation}₽ и в кассе теперь {cash_day}₽", file=ar)
        elif n == 2:
            print(f"{data} Было внесенно {cash_collation}₽ и в кассе теперь {cash_day}₽", file=ar)
        elif n == 3:
            print(f"{data} в кассе {cash_day}₽: была посчитана с результатом {cash_collation}₽", file=ar)



class Ui_Cash_menu(object):
    def setupUi(self, Cash_menu):
        Cash_menu.setObjectName("Cash_menu")
        Cash_menu.resize(650, 450)
        Cash_menu.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(Cash_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Compare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Compare.setGeometry(QtCore.QRect(180, 30, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compare.setFont(font)
        self.pushButton_Compare.setStyleSheet("")
        self.pushButton_Compare.setObjectName("pushButton_Compare")
        self.pushButton_Attach = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Attach.setGeometry(QtCore.QRect(180, 160, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Attach.setFont(font)
        self.pushButton_Attach.setStyleSheet("")
        self.pushButton_Attach.setObjectName("pushButton_Attach")
        self.pushButton_Withdraw = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Withdraw.setGeometry(QtCore.QRect(180, 290, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Withdraw.setFont(font)
        self.pushButton_Withdraw.setStyleSheet("")
        self.pushButton_Withdraw.setObjectName("pushButton_Withdraw")
        Cash_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cash_menu)
        QtCore.QMetaObject.connectSlotsByName(Cash_menu)

    def retranslateUi(self, Cash_menu):
        _translate = QtCore.QCoreApplication.translate
        Cash_menu.setWindowTitle(_translate("Cash_menu", "Касса"))
        self.pushButton_Compare.setText(_translate("Cash_menu", "Сверить"))
        self.pushButton_Attach.setText(_translate("Cash_menu", "Вложить"))
        self.pushButton_Withdraw.setText(_translate("Cash_menu", "Изъять"))


class Ui_Collation(object):
    def setupUi(self, Collation):
        Collation.setObjectName("Collation")
        Collation.resize(650, 450)
        Collation.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(Collation)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5000 = QtWidgets.QLabel(self.centralwidget)
        self.label_5000.setGeometry(QtCore.QRect(20, 10, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5000.setFont(font)
        self.label_5000.setObjectName("label_5000")
        self.label_1000 = QtWidgets.QLabel(self.centralwidget)
        self.label_1000.setGeometry(QtCore.QRect(20, 50, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_1000.setFont(font)
        self.label_1000.setObjectName("label_1000")
        self.label_500 = QtWidgets.QLabel(self.centralwidget)
        self.label_500.setGeometry(QtCore.QRect(20, 90, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_500.setFont(font)
        self.label_500.setObjectName("label_500")
        self.label_100 = QtWidgets.QLabel(self.centralwidget)
        self.label_100.setGeometry(QtCore.QRect(20, 130, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(20, 170, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 330, 230, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.spinBox_5000 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5000.setGeometry(QtCore.QRect(260, 10, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_5000.setFont(font)
        self.spinBox_5000.setObjectName("spinBox_5000")
        self.spinBox_1000 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1000.setGeometry(QtCore.QRect(260, 50, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_1000.setFont(font)
        self.spinBox_1000.setObjectName("spinBox_1000")
        self.spinBox_500 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_500.setGeometry(QtCore.QRect(260, 90, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_500.setFont(font)
        self.spinBox_500.setObjectName("spinBox_500")
        self.spinBox_100 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_100.setGeometry(QtCore.QRect(260, 130, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_100.setFont(font)
        self.spinBox_100.setObjectName("spinBox_100")
        self.spinBox_50 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_50.setGeometry(QtCore.QRect(260, 170, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_50.setFont(font)
        self.spinBox_50.setObjectName("spinBox_50")
        self.spinBox_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_10.setGeometry(QtCore.QRect(260, 210, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_10.setFont(font)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(260, 250, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 290, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(260, 330, 60, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_1.setFont(font)
        self.spinBox_1.setObjectName("spinBox_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 20, 281, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_cash = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_cash.setFont(font)
        self.label_cash.setIndent(10)
        self.label_cash.setObjectName("label_cash")
        self.verticalLayout.addWidget(self.label_cash)
        self.label_Conclusion = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Conclusion.setFont(font)
        self.label_Conclusion.setText("")
        self.label_Conclusion.setIndent(10)
        self.label_Conclusion.setObjectName("label_Conclusion")
        self.verticalLayout.addWidget(self.label_Conclusion)
        self.label_smile = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_smile.setFont(font)
        self.label_smile.setToolTipDuration(-1)
        self.label_smile.setText("")
        self.label_smile.setIndent(10)
        self.label_smile.setObjectName("label_smile")
        self.verticalLayout.addWidget(self.label_smile)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 369, 611, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_check = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_check.setFont(font)
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout.addWidget(self.pushButton_check)
        self.pushButton_menu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout.addWidget(self.pushButton_menu)
        self.pushButton_close = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        Collation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Collation)
        QtCore.QMetaObject.connectSlotsByName(Collation)

    def retranslateUi(self, Collation):
        _translate = QtCore.QCoreApplication.translate
        Collation.setWindowTitle(_translate("Collation", "Сверка"))
        self.label_5000.setText(_translate("Collation", "Введите количество 5000₽ банкнот"))
        self.label_1000.setText(_translate("Collation", "Введите количество 1000₽ банкнот"))
        self.label_500.setText(_translate("Collation", "Введите количество 500₽ банкнот"))
        self.label_100.setText(_translate("Collation", "Введите количество 100₽ банкнот"))
        self.label_50.setText(_translate("Collation", "Введите количество 50₽ банкнот"))
        self.label_10.setText(_translate("Collation", "Введите количество 10₽ монет"))
        self.label_5.setText(_translate("Collation", "Введите количество 5₽ монет"))
        self.label_2.setText(_translate("Collation", "Введите количество 2₽ монет"))
        self.label_1.setText(_translate("Collation", "Введите количество 1₽ монет"))
        self.label_cash.setText(_translate("Collation", f"В кассе: {check()}₽"))
        self.pushButton_check.setText(_translate("Collation", "Проверка"))
        self.pushButton_menu.setText(_translate("Collation", "В меню"))
        self.pushButton_close.setText(_translate("Collation", "Закрыть"))


class Ui_Attach(object):
    def setupUi(self, Attach):
        Attach.setObjectName("Attach")
        Attach.resize(650, 450)
        Attach.setMinimumSize(QtCore.QSize(650, 450))
        Attach.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(Attach)
        self.centralwidget.setMinimumSize(QtCore.QSize(650, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 50, 261, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_attach = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_attach.setFont(font)
        self.pushButton_attach.setObjectName("pushButton_attach")
        self.gridLayout.addWidget(self.pushButton_attach, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.label_cash = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_cash.setFont(font)
        self.label_cash.setIndent(10)
        self.label_cash.setObjectName("label_cash")
        self.gridLayout.addWidget(self.label_cash, 1, 0, 1, 1)
        self.label_sign = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_sign.setFont(font)
        self.label_sign.setObjectName("label_sign")
        self.gridLayout.addWidget(self.label_sign, 2, 1, 1, 1)
        self.label_smile = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_smile.setFont(font)
        self.label_smile.setToolTipDuration(-1)
        self.label_smile.setText("")
        self.label_smile.setIndent(95)
        self.label_smile.setObjectName("label_smile")
        self.gridLayout.addWidget(self.label_smile, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 360, 581, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_menu = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.gridLayout_2.addWidget(self.pushButton_menu, 0, 2, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_2.addWidget(self.pushButton_close, 0, 3, 1, 1)
        Attach.setCentralWidget(self.centralwidget)

        self.retranslateUi(Attach)
        QtCore.QMetaObject.connectSlotsByName(Attach)

    def retranslateUi(self, Attach):
        _translate = QtCore.QCoreApplication.translate
        Attach.setWindowTitle(_translate("Attach", "Вложить"))
        self.pushButton_attach.setText(_translate("Attach", "Вложить"))
        self.label_cash.setText(_translate("Attach", "В кассе: 0"))
        self.label_sign.setText(_translate("Attach", "₽"))
        self.pushButton_menu.setText(_translate("Attach", "В меню"))
        self.pushButton_close.setText(_translate("Attach", "Закрыть"))


class Ui_Withdraw(object):
    def setupUi(self, Withdraw):
        Withdraw.setObjectName("Withdraw")
        Withdraw.resize(650, 450)
        self.centralwidget = QtWidgets.QWidget(Withdraw)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 60, 261, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_withdraw = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_withdraw.setFont(font)
        self.pushButton_withdraw.setObjectName("pushButton_withdraw")
        self.gridLayout.addWidget(self.pushButton_withdraw, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.label_cash = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_cash.setFont(font)
        self.label_cash.setIndent(10)
        self.label_cash.setObjectName("label_cash")
        self.gridLayout.addWidget(self.label_cash, 1, 0, 1, 1)
        self.label_sign = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_sign.setFont(font)
        self.label_sign.setObjectName("label_sign")
        self.gridLayout.addWidget(self.label_sign, 2, 1, 1, 1)
        self.label_smile = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_smile.setFont(font)
        self.label_smile.setToolTipDuration(-1)
        self.label_smile.setText("")
        self.label_smile.setIndent(95)
        self.label_smile.setObjectName("label_smile")
        self.gridLayout.addWidget(self.label_smile, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 350, 581, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_menu = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.gridLayout_2.addWidget(self.pushButton_menu, 0, 2, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_2.addWidget(self.pushButton_close, 0, 3, 1, 1)
        Withdraw.setCentralWidget(self.centralwidget)

        self.retranslateUi(Withdraw)
        QtCore.QMetaObject.connectSlotsByName(Withdraw)

    def retranslateUi(self, Withdraw):
        _translate = QtCore.QCoreApplication.translate
        Withdraw.setWindowTitle(_translate("Withdraw", "Изъять"))
        self.pushButton_withdraw.setText(_translate("Withdraw", "Изъять"))
        self.label_cash.setText(_translate("Withdraw", "В кассе: 0"))
        self.label_sign.setText(_translate("Withdraw", "₽"))
        self.pushButton_menu.setText(_translate("Withdraw", "В меню"))
        self.pushButton_close.setText(_translate("Withdraw", "Закрыть"))


app = QtWidgets.QApplication(sys.argv)

Cash_menu = QtWidgets.QMainWindow()
ui = Ui_Cash_menu()
ui.setupUi(Cash_menu)
Cash_menu.show()


def return_menu(n):
    def return_menu_1():
        collation.close()
        Cash_menu.show()

    def return_menu_2():
        attach.close()
        Cash_menu.show()

    def return_menu_3():
        withdraw.close()
        Cash_menu.show()

    if n == 1:
        return_menu_1()
    elif n == 2:
        return_menu_2()
    elif n == 3:
        return_menu_3()


def close(n):
    def close_1():
        collation.close()
        sys.exit(app.exec_())

    def close_2():
        attach.close()
        sys.exit(app.exec_())

    def close_3():
        withdraw.close()
        sys.exit(app.exec_())

    if n == 1:
        close_1()
    elif n == 2:
        close_2()
    elif n == 3:
        close_3()


def open_collation():
    global collation
    collation = QtWidgets.QMainWindow()
    ui = Ui_Collation()
    ui.setupUi(collation)
    Cash_menu.close()
    collation.show()

    def kas():
        cash_day = check()
        cash_5000 = int(ui.spinBox_5000.text()) * 5000
        cash_1000 = int(ui.spinBox_1000.text()) * 1000
        cash_500 = int(ui.spinBox_500.text()) * 500
        cash_100 = int(ui.spinBox_100.text()) * 100
        cash_50 = int(ui.spinBox_50.text()) * 50
        cash_10 = int(ui.spinBox_10.text()) * 10
        cash_5 = int(ui.spinBox_5.text()) * 5
        cash_2 = int(ui.spinBox_2.text()) * 2
        cash_1 = int(ui.spinBox_1.text())
        cash_day2 = cash_5000 + cash_1000 + cash_500 + cash_100 + cash_50 + cash_10 + cash_5 + cash_2 + cash_1
        cash_collation = cash_day2 - cash_day

        if cash_collation == 0:
            ui.label_Conclusion.setText("Касса ровная!!!")
            ui.label_smile.setText("(◕‿◕)")
        elif cash_collation > 0:
            ui.label_Conclusion.setText(f"Удалити из кассы +{cash_collation}")
            ui.label_smile.setText("(ಠ_ಠ)")
        elif cash_collation < 0:
            ui.label_Conclusion.setText(f"В кассе {cash_collation}₽")
            ui.label_smile.setText("┌( ಠ_ಠ)┘")

        archive(3, time_date(), cash_day, cash_collation)

    ui.pushButton_check.clicked.connect(kas)
    ui.pushButton_menu.clicked.connect(lambda: return_menu(1))
    ui.pushButton_close.clicked.connect(lambda: close(1))


def open_attach():
    global attach
    attach = QtWidgets.QMainWindow()
    ui = Ui_Attach()
    ui.setupUi(attach)
    Cash_menu.close()
    attach.show()

    def attach_1():
        cash_day_1 = check()
        cash_day_2 = int(ui.lineEdit.text())
        cash_day = cash_day_1 + cash_day_2
        check_z(cash_day)
        ui.label_cash.setText(f"В кассе: {check()}₽")
        ui.label_smile.setText("(◕‿◕)")
        archive(2, time_date(), cash_day, cash_day_2)

    ui.pushButton_attach.clicked.connect(attach_1)
    ui.pushButton_menu.clicked.connect(lambda: return_menu(2))
    ui.pushButton_close.clicked.connect(lambda: close(2))

    ui.label_cash.setText(f"В кассе: {check()}₽")


def open_withdraw():
    global withdraw
    withdraw = QtWidgets.QMainWindow()
    ui = Ui_Withdraw()
    ui.setupUi(withdraw)
    Cash_menu.close()
    withdraw.show()

    def withdraw_1():
        cash_day_1 = check()
        cash_day_2 = int(ui.lineEdit.text())
        cash_day = cash_day_1 - cash_day_2
        check_z(cash_day)
        ui.label_cash.setText(f"В кассе: {check()}₽")
        ui.label_smile.setText("(◕‿◕)")
        archive(1, time_date(), cash_day, cash_day_2)

    ui.pushButton_withdraw.clicked.connect(withdraw_1)
    ui.pushButton_menu.clicked.connect(lambda: return_menu(3))
    ui.pushButton_close.clicked.connect(lambda: close(3))

    ui.label_cash.setText(f"В кассе: {check()}₽")




ui.pushButton_Compare.clicked.connect(open_collation)
ui.pushButton_Attach.clicked.connect(open_attach)
ui.pushButton_Withdraw.clicked.connect(open_withdraw)


sys.exit(app.exec_())
