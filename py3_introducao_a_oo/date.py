class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def format_date(self):
        print(f"{self.__day}/{self.__month}/{self.__year}")

    def getDay(self):
        return self.__day

    def getMonth(self):
        return self.__month

    def getYear(self):
        return self.__year
