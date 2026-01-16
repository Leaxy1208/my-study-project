"""! 
    @mainpage sadsa
    sadsad
    sad
    sadsaddsa
"""
import sys
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QTabWidget
from PyQt5.QtGui import QPalette, QColor

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(500, 300)

    def initUI(self):
        self.setWindowTitle('Калькулятор обмена валют')

        self.base_currency_input = QLineEdit(self)
        self.base_currency_input.setPlaceholderText('Введите переводимую валюту (например,USD)')

        self.target_currency_input = QLineEdit(self)
        self.target_currency_input.setPlaceholderText('Введите валюту, в которую переводите (например,EUR)')

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText('Сумма для обмена')

        self.result_label = QLabel(self)

        self.convert_button = QPushButton('Конвертировать', self)
        self.convert_button.clicked.connect(self.convert_currency)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Валюта из которой хотите перевести:'))
        layout.addWidget(self.base_currency_input)
        layout.addWidget(QLabel('Валюта в которую переводите:'))
        layout.addWidget(self.target_currency_input)
        layout.addWidget(QLabel('Сумма для обмена:'))
        layout.addWidget(self.amount_input)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_exchange_rate(self, base_currency, target_currency):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Ошибка при получении данных с API")

        data = response.json()
        if base_currency in data['Valute'] and target_currency in data['Valute']:
            base_rate = data['Valute'][base_currency]['Value']
            target_rate = data['Valute'][target_currency]['Value']
            return target_rate / base_rate
        else:
            return None

    def convert_currency(self):
        base_currency = self.base_currency_input.text().upper()
        target_currency = self.target_currency_input.text().upper()
        amount_str = self.amount_input.text().strip()

        try:
            if not base_currency or not target_currency or not amount_str:
                self.result_label.setText("Заполните все поля.")
                return
            
            amount = float(amount_str)

            rate = self.get_exchange_rate(base_currency, target_currency)
            if rate:
                converted_amount = amount * rate
                self.result_label.setText(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            else:
                self.result_label.setText("Недоступный курс для указанной валюты.")
        except ValueError:
            self.result_label.setText("Введите корректную сумму.")
        except Exception as e:
            self.result_label.setText("Соединение прервано, попробуйте конвертировать еще раз.")

class TaxCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор налога УСН')

        self.year_input = QLineEdit(self)
        self.year_input.setPlaceholderText('2025')

        self.revenue_quarter1_input = QLineEdit(self)
        self.revenue_quarter1_input.setPlaceholderText('Доходы 1 квартал')

        self.revenue_quarter2_input = QLineEdit(self)
        self.revenue_quarter2_input.setPlaceholderText('Доходы 2 квартал')

        self.revenue_quarter3_input = QLineEdit(self)
        self.revenue_quarter3_input.setPlaceholderText('Доходы 3 квартал')

        self.revenue_quarter4_input = QLineEdit(self)
        self.revenue_quarter4_input.setPlaceholderText('Доходы 4 квартал')

        self.expense_quarter1_input = QLineEdit(self)
        self.expense_quarter1_input.setPlaceholderText('Расходы 1 квартал')

        self.expense_quarter2_input = QLineEdit(self)
        self.expense_quarter2_input.setPlaceholderText('Расходы 2 квартал')

        self.expense_quarter3_input = QLineEdit(self)
        self.expense_quarter3_input.setPlaceholderText('Расходы 3 квартал')

        self.expense_quarter4_input = QLineEdit(self)
        self.expense_quarter4_input.setPlaceholderText('Расходы 4 квартал')

        self.advance_quarter1_input = QLineEdit(self)
        self.advance_quarter1_input.setPlaceholderText('Авансовые платежи 1 квартал')

        self.advance_quarter2_input = QLineEdit(self)
        self.advance_quarter2_input.setPlaceholderText('Авансовые платежи 2 квартал')

        self.advance_quarter3_input = QLineEdit(self)
        self.advance_quarter3_input.setPlaceholderText('Авансовые платежи 3 квартал')

        self.advance_quarter4_input = QLineEdit(self)
        self.advance_quarter4_input.setPlaceholderText('Авансовые платежи 4 квартал')

        self.tax_rate_input = QLineEdit(self)
        self.tax_rate_input.setPlaceholderText('Ставка налога (например, 6)')

        self.result_label = QLabel(self)

        self.calculate_button = QPushButton('Рассчитать налог', self)
        self.calculate_button.clicked.connect(self.calculate_tax)
        self.calculate_button.setFixedSize(705, 40)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Отчетный год:'))
        layout.addWidget(self.year_input)

        layout.addWidget(QLabel('Доходы по кварталам:'))
        layout.addWidget(self.revenue_quarter1_input)
        layout.addWidget(self.revenue_quarter2_input)
        layout.addWidget(self.revenue_quarter3_input)
        layout.addWidget(self.revenue_quarter4_input)

        layout.addWidget(QLabel('Расходы по кварталам:'))
        layout.addWidget(self.expense_quarter1_input)
        layout.addWidget(self.expense_quarter2_input)
        layout.addWidget(self.expense_quarter3_input)
        layout.addWidget(self.expense_quarter4_input)

        layout.addWidget(QLabel('Авансовые платежи по кварталам:'))
        layout.addWidget(self.advance_quarter1_input)
        layout.addWidget(self.advance_quarter2_input)
        layout.addWidget(self.advance_quarter3_input)
        layout.addWidget(self.advance_quarter4_input)

        layout.addWidget(QLabel('Ставка налога (в %):'))
        layout.addWidget(self.tax_rate_input)

        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_tax(self):
        try:
            year = int(self.year_input.text())
            tax_rate = float(self.tax_rate_input.text()) / 100

            revenue_quarter1 = float(self.revenue_quarter1_input.text() or 0)
            revenue_quarter2 = float(self.revenue_quarter2_input.text() or 0)
            revenue_quarter3 = float(self.revenue_quarter3_input.text() or 0)
            revenue_quarter4 = float(self.revenue_quarter4_input.text() or 0)

            expense_quarter1 = float(self.expense_quarter1_input.text() or 0)
            expense_quarter2 = float(self.expense_quarter2_input.text() or 0)
            expense_quarter3 = float(self.expense_quarter3_input.text() or 0)
            expense_quarter4 = float(self.expense_quarter4_input.text() or 0)

            advance_quarter1 = float(self.advance_quarter1_input.text() or 0)
            advance_quarter2 = float(self.advance_quarter2_input.text() or 0)
            advance_quarter3 = float(self.advance_quarter3_input.text() or 0)
            advance_quarter4 = float(self.advance_quarter4_input.text() or 0)

            total_revenue = (revenue_quarter1 + revenue_quarter2 +
                             revenue_quarter3 + revenue_quarter4)

            total_expenses = (expense_quarter1 + expense_quarter2 +
                              expense_quarter3 + expense_quarter4)

            total_advanced_payments = (advance_quarter1 + advance_quarter2 +
                                       advance_quarter3 + advance_quarter4)

            profit = total_revenue - total_expenses
            tax_due = profit * tax_rate if profit > 0 else 0

            total_tax = tax_due - total_advanced_payments
            total_tax = max(total_tax, 0)

            self.result_label.setText(f'Итоговый налог к уплате: {total_tax:.2f} рублей')
        except ValueError:
            self.result_label.setText('Ошибка: пожалуйста, введите корректные числовые значения.')

class CurrencyFetcher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Курсы валют ЦБРФ')

        self.base_currency_input = QLineEdit(self)
        self.base_currency_input.setPlaceholderText('Введите код валюты (например, USD)')

        self.fetch_button = QPushButton('Получить курс', self)
        self.fetch_button.clicked.connect(self.fetch_currency)

        self.result_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.base_currency_input)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def fetch_currency(self):
        base_currency = self.base_currency_input.text().upper()

        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            rates = data['Valute']
            currency = rates.get(base_currency)

            if currency:
                self.result_label.setText(f'Курс {base_currency}: {currency["Value"]:.2f} руб.')
            else:
                self.result_label.setText('Курс указанной валюты не найден.')

        except requests.exceptions.RequestException as e:
            self.result_label.setText(f'Ошибка сети: {e}')
        except ValueError:
            self.result_label.setText('Ошибка обработки данных.')

class CurrencyGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('График курсов валют')

        self.start_date_input = QLineEdit(self)
        self.start_date_input.setPlaceholderText('Начальная дата (дд.мм.гггг)')

        self.end_date_input = QLineEdit(self)
        self.end_date_input.setPlaceholderText('Конечная дата (дд.мм.гггг)')

        self.currency_code_input = QLineEdit(self)
        self.currency_code_input.setPlaceholderText('Введите код валюты (например, R01235)')

        self.fetch_button = QPushButton('Построить график', self)
        self.fetch_button.clicked.connect(self.plot_graph)

        self.result_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Укажите диапазон дат:'))
        layout.addWidget(self.start_date_input)
        layout.addWidget(self.end_date_input)
        layout.addWidget(QLabel('Код валюты (например, R01235):'))
        layout.addWidget(self.currency_code_input)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def plot_graph(self):
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()
        currency_code = self.currency_code_input.text()

        url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date}&date_req2={end_date}&VAL_NM_RQ={currency_code}"

        try:
            response = requests.get(url)
            data = response.content
            root = ET.fromstring(data)

            dates = []
            values = []

            for item in root.findall('Record'):
                date = item.get('Date')
                value = float(item.find('Value').text.replace(',', '.'))
                dates.append(datetime.strptime(date, '%d.%m.%Y'))
                values.append(value)

            plt.style.use('dark_background')
            plt.figure(figsize=(10, 5))
            plt.plot(dates, values, marker='o')

            plt.gcf().canvas.manager.set_window_title(f'График курсов валют {currency_code}')
            plt.title(f'Курс валюты с {start_date} по {end_date}', color='white')
            plt.xlabel('Дата', color='white')
            plt.ylabel('Курс валюты', color='white')
            plt.xticks(rotation=30, color='white')
            plt.yticks(color='white')
            plt.grid(color='gray')
            plt.tight_layout()

            plt.show()
        except Exception as e:
            self.result_label.setText('Ошибка при получении данных или построении графика.')


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(750, 600)

    def initUI(self):
        self.setWindowTitle('Конвертор')

        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 rgba(0, 0, 0, 255), 
                    stop: 1 rgba(0, 0, 128, 255)); /* Dark blue */
                color: white; /* Set text color to white for visibility */
            }
            QTabWidget {
                background-color: black; /* Tab widget background color */
                color: white; /* Text color for tabs */
            }
            QTabBar {
                background-color: black; /* Tab bar background */
                padding: 5px;
            }
            QTabBar::tab {
                background: black; /* Individual tab background */
                color: white; /* Individual tab text color */
                padding: 10px;
                border: 1px solid rgba(255, 255, 255, 0.5); /* Optional border */
            }
            QTabBar::tab:selected {
                background: rgba(0, 0, 128, 255); /* Highlight selected tab */
                color: white; /* Selected tab text color */
            }
            QPushButton {
                background-color: black; /* Button background color */
                color: white; /* Button text color */
                border: 1px solid rgba(255, 255, 255, 0.5); /* Optional border */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(50, 50, 50, 255); /* Darker shade on hover */
            }
        """)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(10, 10, 730, 550)

        self.currency_converter_tab = CurrencyConverter()
        self.tab_widget.addTab(self.currency_converter_tab, "Калькулятор валют")

        self.tax_calculator_tab = TaxCalculator()
        self.tab_widget.addTab(self.tax_calculator_tab, "Калькулятор налога УСН")

        self.currency_fetcher_tab = CurrencyFetcher()
        self.tab_widget.addTab(self.currency_fetcher_tab, "Курсы валют")

        self.currency_graph_tab = CurrencyGraph()
        self.tab_widget.addTab(self.currency_graph_tab, "График курсов валют")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())