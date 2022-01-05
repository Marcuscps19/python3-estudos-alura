from date import Date
from client import Client


class Account:
    def __init__(self, number, owner, balance, limit=1000.0):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def extrato(self):
        print(f"Saldo {self.__balance} do titular {self.__owner}")

    def deposita(self, value):
        self.__balance += value

    def saca(self, value):
        balance_antigo = self.__balance
        if(self.__balance >= value):
            self.__balance -= value
            print(f"Valor sacado: {value}")
            print(f"Saldo antigo: {balance_antigo}")
            print(f"Saldo atual: {self.__balance}")

    def transfere(self, value, destination):
        self.saca(value)
        destination.deposita(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def set_limit(self, limit):
        self.__limit = limit


if(__name__ == '__main__'):
    conta = Account(1, 'Marcus', 10)
    conta2 = Account(2, 'Mayra', 10)
    conta.transfere(10, conta2)
    print(conta.extrato())
    print(conta2.extrato())
    new_date = Date(12, 2, 1992)
    new_date.format_date()
    client = Client('Marcus')
    print(client.name)
    client.name = 'mayra'
    print(client.name)
