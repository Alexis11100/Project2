from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """This class initializes the buttons and sets the balance up for later"""
    def __init__(self):
        super().__init__()
        self.balance = None
        self.setupUi(self)
        self.search_btn.clicked.connect(lambda: self.search())
        self.deposit_btn.clicked.connect(lambda: self.deposit())

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
                        self.acct_bal.setStyleSheet("color:black;")
                        self.acct_bal.setText(f'Your account balance is {self.balance:.2f}')
                        return

        self.acct_bal.setText("Account not found.")
        self.acct_bal.setStyleSheet("color: red;")

    def deposit(self):
        try:
            amount = float(self.amount.text())
        except ValueError:
            self.acct_bal.setStyleSheet("color: red;")
            self.acct_bal.setText("Invalid amount entered.")
            return

        if self.balance is None:
            self.acct_bal.setStyleSheet("color: red;")
            self.acct_bal.setText("No account selected. Please search first.")
            return

        if amount >= 0:
            self.balance += amount
            self.acct_bal.setStyleSheet("color: black;")
            self.acct_bal.setText(
                f'You have deposited ${amount:.2f}\nYour new balance is ${self.balance:.2f}'
            )
        else:
            self.acct_bal.setStyleSheet("color: red;")
            self.acct_bal.setText("The amount entered is invalid. Please try again.")















