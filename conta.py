from date import Date


class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, value):
        self.__saldo += value

    def saca(self, value):
        saldo_antigo = self.__saldo
        if(self.__saldo >= value):
            self.__saldo -= value
            print(f"Valor sacado: {value}")
            print(f"Saldo antigo: {saldo_antigo}\nSaldo atual: {self.__saldo}")

    # def transfere(self, value, )


if(__name__ == '__main__'):
    conta = Conta(1, 'Marcus', 10)
    conta.extrato()
    conta.deposita(1)
    conta.saca(2)
    conta.saca(2000)
    new_date = Date(12, 2, 1992)
    new_date.format_date()
