from datetime import datetime
from modules.databaseUtilities import databaseUtilities

class Database():
    def __init__(self, dataFromDatabase):
        self.db = databaseUtilities()
        self.db.createDatabase(dataFromDatabase)
        self.db.drawTable("stock", "(id text PRIMARY KEY, symbol text, date text, open text, high text, low text, close integer, volume integer)")

    def close(self):
        self.db.connection.close()

    def addStocks(self,Symbol,Date,Open,High,Low,Close,Volume):
        stockID = f"{Symbol}_{Date}".lower()
        dateFormatted = datetime.strptime(Date, '%d-%b-%y').date().strftime('%Y-%m-%d')

        self.db.insertIntoTable("stock", "VALUES (?,?,?,?,?,?,?,?)", (
            stockID,
            Symbol,
            dateFormatted,
            Open,
            High,
            Low,
            Close,
            Volume
        ))

    def getStocks(self, symbol=None):
        stockFilter = f'WHERE symbol="{symbol}"' if symbol else ''
        return self.db.getData(f'SELECT symbol, date, open, high, low, close, volume FROM stock {stockFilter} ORDER BY date ASC')     

    def addInvestment(self, stocks_list):
        for stock in stocks_list:
            self.addStocks(*list(stock.values()))



