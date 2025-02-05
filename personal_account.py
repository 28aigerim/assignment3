from amount import Amount
import datetime

class PersonalAccount:

    def __init__(self, __account_number, __account_holder, __balance =0, transactions=[]):
        #self.__account_number = account_number
        #self.__account_holder = account_holder
        self.__balance = 0
        self.transactions = []

    def deposit(self, amount):
        deposit1 = Amount(amount, datetime.datetime.now, 'DEPOSIT')
        self.transactions.append(deposit1)
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            withdraw1 = Amount(amount, datetime.datetime.now, 'WITHDRAWAL')
            self.transactions.append(withdraw1)
            self.balance -= amount

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
            print()

    def get_balance(self):
        print(f'The current balance is {self.balance}.')

    def get_account_number(self):
        print(f'The account number is {self.account_number}.')

    def set_account_number(self, account_number):
        self.account_number = int(input('Enter a new account number: '))

    def get_account_holder(self):
        print(f'The account holder is {self.account_holder}.')

    def set_account_holder(self, account_holder):
        self.account_holder = input('Enter the new account holder: ')

    def __str__(self):
        return f'Personal account {self.account_number} is holded by {self.account_holder}. The current balance is {self.balance}.'

    def __add__(self, amount):
        deposit1 = Amount(amount, datetime.datetime.now, 'DEPOSIT')
        self.transactions.append(deposit1)
        self.balance += amount
        return self

    def __sub__(self, amount):
        if amount >= self.balance:
            withdraw1 = Amount(amount, datetime.datetime.now, 'WITHDRAWAL')
            self.transactions.append(withdraw1)
            self.balance -= amount
        return self
