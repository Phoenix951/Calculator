# Мой калькулятор

# Импортируемые модули
import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

# Импортирование дизайна
from calcul_design import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Конструктор"""
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.required_oper = None
        self.Number = None
        self.firstNumber = None
        self.key = "0"

        # кнопки операций
        self.plusButton.clicked.connect(self.all_operation)
        self.minusButton.clicked.connect(self.all_operation)
        self.multButton.clicked.connect(self.all_operation)
        self.divideButton.clicked.connect(self.all_operation)
        self.radicalButton.clicked.connect(self.all_operation)
        self.degreeButton.clicked.connect(self.all_operation)
        self.degreeToYButton.clicked.connect(self.all_operation)
        self.sinButton.clicked.connect(self.all_operation)
        self.thirdRadicalButton.clicked.connect(self.all_operation)     
        self.reverseButton.clicked.connect(self.all_operation)
        self.procentButton.clicked.connect(self.all_operation)
        self.exponButton.clicked.connect(self.constants)
        self.numPIButton.clicked.connect(self.constants)
        self.intInFloat.clicked.connect(self.int_in_float)
        self.equalButton.clicked.connect(self.equal_operation)
        self.clearAll.clicked.connect(self.new_number)
        self.deleteItem.clicked.connect(self.delete_item)

        # кнопки чисел
        self.oneBut.clicked.connect(self.oneButton)
        self.twoBut.clicked.connect(self.twoButton)
        self.threeBut.clicked.connect(self.threeButton)
        self.fourBut.clicked.connect(self.fourButton)
        self.fiveBut.clicked.connect(self.fiveButton)
        self.sixBut.clicked.connect(self.sixButton)
        self.sevenBut.clicked.connect(self.sevenButton)
        self.eightBut.clicked.connect(self.eightButton)
        self.nineBut.clicked.connect(self.nineButton)
        self.zeroBut.clicked.connect(self.zeroButton)

    def firstLineItem(self, number):
        """Метод создания числа в поле"""
        self.Number = self.resultLine.text()
        self.Number += number
        return self.Number

    def int_in_float(self):
        Item = "."
        number = self.resultLine.text()
        if "." in number:
            self.resultLine.setText(self.firstLineItem(""))
        else:
            self.resultLine.setText(self.firstLineItem(Item))
        
    def oneButton(self):
        Item = "1"
        self.resultLine.setText(self.firstLineItem(Item))

    def twoButton(self):
        Item = "2"
        self.resultLine.setText(self.firstLineItem(Item))

    def threeButton(self):
        Item = "3"
        self.resultLine.setText(self.firstLineItem(Item))

    def fourButton(self):
        Item = "4"
        self.resultLine.setText(self.firstLineItem(Item))

    def fiveButton(self):
        Item = "5"
        self.resultLine.setText(self.firstLineItem(Item))

    def sixButton(self):
        Item = "6"
        self.resultLine.setText(self.firstLineItem(Item))

    def sevenButton(self):
        Item = "7"
        self.resultLine.setText(self.firstLineItem(Item))

    def eightButton(self):
        Item = "8"
        self.resultLine.setText(self.firstLineItem(Item))

    def nineButton(self):
        Item = "9"
        self.resultLine.setText(self.firstLineItem(Item))

    def zeroButton(self):
        Item = "0"
        self.resultLine.setText(self.firstLineItem(Item))

    def constants(self):
        """Метод для обработки нажатия кнопок констант"""
        sender = self.sender()
        if sender.text() == "exp":
            expon = math.e
            self.resultLine.setText(str(expon))
        elif sender.text() == "pi":
            numPi = math.pi
            self.resultLine.setText(str(numPi))

    def all_operation(self):
        """Метод для обработки нажатий кнопок требуемых операций"""
        sender = self.sender()
        if sender.text() == "+":
            self.required_oper = "plus"
        elif sender.text() == "-":
            self.required_oper = "minus"
        elif sender.text() == "*":
            self.required_oper = "mult"
        elif sender.text() == "/":
            self.required_oper = "div"
        elif sender.text() == "sqrt(x)":
            self.required_oper = "sqrt"
        elif sender.text() == "x^2":
            self.required_oper = "degr"
        elif sender.text() == "x^y":
            self.required_oper = "degrToY"
        elif sender.text() == "sin(x)":
            self.required_oper = "sin"
        elif sender.text() == "3sqrt(x)":
            self.required_oper = "3sqrt"
        elif sender.text() == "1/x":
            self.required_oper = "1/x"
        elif sender.text() == "%":
            self.required_oper = "procent"

        if self.Number == None:
            self.Number = self.resultLine.text()
            self.firstLineNumber = self.Number
        else:
            self.firstLineNumber = self.Number
        self.Number = None
        self.resultLine.clear()
        
    def equal_operation(self):
        """Метод для выведения результата (нажатие кнопки '=')"""
        if self.Number == None:
            self.Number = self.resultLine.text()

        # операция сложения
        if self.required_oper == "plus" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = self.firstNumber + self.secondNumber
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "plus" and self.key == "1":
            self.result = self.firstNumber + self.secondNumber
            self.firstNumber = self.result
        # операция вычитания
        elif self.required_oper == "minus" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = self.firstNumber - self.secondNumber
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "minus" and self.key == "1":
            self.result = self.firstNumber - self.secondNumber
            self.firstNumber = self.result
        # операция умножения
        elif self.required_oper == "mult" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = self.firstNumber * self.secondNumber
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "mult" and self.key == "1":
            self.result = self.firstNumber * self.secondNumber
            self.firstNumber = self.result
        # операция деления
        elif self.required_oper == "div" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = self.firstNumber // self.secondNumber
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "div" and self.key == "1":
            self.result = self.firstNumber // self.secondNumber
            self.firstNumber = self.result
        # операция возведения в степень 2
        elif self.required_oper == "degr" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.result = self.firstNumber ** 2
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "degr" and self.key == "1":
            self.result = self.firstNumber ** 2
            self.firstNumber = self.result
        # операция возведения в степень y
        elif self.required_oper == "degrToY" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = self.firstNumber ** self.secondNumber
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "degrToY" and self.key == "1":
            self.result = self.firstNumber ** self.secondNumber
            self.firstNumber = self.result
        # операция вывода из под корня
        elif self.required_oper == "sqrt":
            self.firstNumber = float(self.firstLineNumber)
            self.result = math.sqrt(self.firstNumber)
        # операция вычисления синуса
        elif self.required_oper == "sin":
            self.firstNumber = float(self.firstLineNumber)
            self.result = math.sin(self.firstNumber * math.pi / 180)
        # операция вычисления кубического корня
        elif self.required_oper == "3sqrt":
            self.firstNumber = float(self.firstLineNumber)
            self.result = math.pow(self.firstNumber, 1/3)
        # операция перевода числа в дробь
        elif self.required_oper == "1/x" and self.key == "0":
            self.firstNumber = float(self.firstLineNumber)
            self.result = (1 / self.firstNumber)
            self.firstNumber = self.result
            self.key = "1"
        elif self.required_oper == "1/x" and self.key == "1":
            self.result = (1 / self.firstNumber)
            self.firstNumber = self.result
        # операция вычисления процента от числа
        elif self.required_oper == "procent":
            self.firstNumber = float(self.firstLineNumber)
            self.secondNumber = float(self.Number)
            self.result = (self.secondNumber * (0.01 * self.firstNumber))
  
        self.resultLine.clear()
        self.resultLine.setText(str(self.result))

    def delete_item(self):
        """Метод для удаления одного элемента"""
        delItem = self.resultLine.text()
        delItem = delItem[:-1]
        self.resultLine.setText(delItem)
        self.Number = self.resultLine.text()
        
    def new_number(self):
        """Метод для удаления всех значений"""
        self.resultLine.clear()
        self.operation = None
        self.Number = None
        self.firstNumber = None
        self.key = "0"

def my_excepthook(type, value, tback):
    """Метод для перехвата ошибок"""
    QtWidgets.QMessageBox.critical(
        main, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )
    sys.__excepthook__(type, value, tback)
 
sys.excepthook = my_excepthook

def main():
    """Метод для выполнения программы"""
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
        
