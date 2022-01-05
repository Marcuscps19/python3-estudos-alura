from date import Date
from client import Client


class Account:
    def __init__(self, number, owner, balance, limit=1000.0):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print(f"Saldo {self.__balance} do titular {self.__owner}")

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value):
        available_for_withdraw = self.__balance + self.__limit
        return (available_for_withdraw >= value)

    def withdraw(self, value):
        old_balance = self.__balance
        if(self.__can_withdraw(value)):
            self.__balance -= value
            print(f"Valor sacado: {value}")
            print(f"Saldo antigo: {old_balance}")
            print(f"Saldo atual: {self.__balance}")

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def banks_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @limit.setter
    def set_limit(self, limit):
        self.__limit = limit


if(__name__ == '__main__'):
    client = Client('Marcus')
    conta = Account(1, client.name, 10)
    print(conta.extract())
    new_date = Date(12, 2, 1992)
    new_date.format_date()
    print(Account.bank_code())
    print(Account.banks_codes())
