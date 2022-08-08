from datetime import datetime

class Stock():
    def __init__(self, symbols, numShares, color, date, priceEOD):
        self.name = symbols.upper()
        self.numShares = numShares
        self.stockID = f"{symbols}_{date}".lower()
        self.color = color

        self.years = []
        self.priceEODList = []
        self.priceNowList = []

        self.createList(date, priceEOD)

    def priceNowFunc(self, priceEOD):
        return (self.numShares * priceEOD)

    def createList(self, date, priceEOD):
        yearAndMonth = datetime.strptime(date, '%d-%b-%y').date().strftime('%Y-%m')

        self.years.append(yearAndMonth)
        self.priceEODList.append(float(priceEOD))
        self.priceNowList.append(self.priceNowFunc(priceEOD))
