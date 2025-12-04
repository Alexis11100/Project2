from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.balance = None
        self.setupUi(self)
        self.search_btn.clicked.connect(lambda: self.search())

    def search(self):
        """This function searches for the first name and last name in the text file and if the first and last
        name is not in the text file it gives the option to create a new account otherwise it displays an error message"""
        with open("accounts.txt", "r") as file:
            first_name = self.first_name.text()
            last_name = self.last_name.text()
            for row in file:
                parts = row.strip().split()  # ["John", "Smith", "1520.75"]
                if len(parts) == 3:
                    account_first_name, account_last_name, account_balance = parts
                    if account_first_name == first_name and account_last_name == last_name:
                        self.balance = float(account_balance)
                        self.acct_bal.setText(f'Your account balance is {self.balance:.2f}')
                        return
                    else:
                        self.acct_bal.setStyleSheet("color: red;")
                        self.acct_bal.setText("Account not found.")
    def deposit(self):
















