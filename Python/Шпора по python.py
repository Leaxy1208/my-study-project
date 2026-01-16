import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel

class Calc (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI (self):
        
        self.first = QLineEdit(self)
        self.first.setPlaceholderText("Введите 1 число")

        self.vtoroe = QLineEdit(self)
        self.vtoroe.setPlaceholderText('Введите 2 число')

        self.output = QLineEdit(self)
        self.output.setPlaceholderText('Итог')
        self.output.setReadOnly(True) # Делаем это поле только для чтения (Чисто итог только для чтения, не для именения)

        self.button = QPushButton ('Cложение', self)
        self.button.clicked.connect(self.plus)
        self.button.setFixedSize(100,100)
        
        self.button1 = QPushButton ('Вычитание', self)
        self.button1.clicked.connect(self.minus)
        self.button1.setFixedSize(100,100)





        #Это нужно для того что бы кнопки были вертикально расположенны и не наложенны друг на друга, так же есть QHBoxLayout (Горизонтальная компоновка), QGridLayout (Сеточная компоновка)
        ''' layout = QGridLayout()
        layout.addWidget(self.button1, 0, 0)  # Первая строка, первый столбец
        layout.addWidget(self.button2, 0, 1)  # Первая строка, второй столбец
        layout.addWidget(self.button3, 1, 0)  # Вторая строка, первый столбец '''
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Название строки"))
        layout.addWidget(self.first)
        layout.addWidget(self.vtoroe)
        layout.addWidget(self.output)
        

        layout.addWidget(self.button)
        layout.addWidget(self.button1)



        self.setLayout(layout)
# что бы поменять местами что-то, нужно менять местами layout'ы
    def plus(self):
        try:
            # Извлечение значений из полей ввода
            num1 = float(self.first.text())
            num2 = float(self.vtoroe.text())
            # Сложение чисел
            result = num1 + num2
            # Отображение результата
            self.output.setText(str(result))
        except ValueError:
            self.output.setText("Ошибка ввода")  # Обработка ошибки при некорректном вводе
     
    def minus(self):
        try:
            num1 = float(self.first.text())
            num2 = float(self.vtoroe.text())
            result1 = num1 - num2
            self.output.setText(str(result1))
        except ValueError:
            self.output.setText('Ошибка ввода')

# для умножения - *, деления -  / (плавающая точка), // (целочисленное деление)

# Это все тупо настройки окна
class MyApp (QWidget):  #Это нужно для создания окна
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self): # Смена имени окна
        self.setWindowTitle("Proba")

if __name__ == '__main__':   # Это нужно для создания окна
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    
    calc = Calc()  # Создайте экземпляр класса Calc
    calc.setParent(ex)  # Установите MyApp как родительский виджет для Calc
    calc.show()  # Отобразите калькулятор
    
    sys.exit(app.exec_())