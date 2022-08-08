from datetime import datetime
from modules.databaseUtilities import databaseUtilities

class Database():
    def __init__(self, db_file):
        self.db = databaseUtilities()
        self.db.create_db(db_file)

        # stock table
        self.db.create_table("stock", "(id text PRIMARY KEY, symbol text, date text, open text, high text, low text, close integer, volume integer)")

    def close(self):
        self.db.connection.close()

    def addInvestment(self, stocks_list):
        for stock in stocks_list:
            self.add_stock(*list(stock.values()))

    def add_stock(self,Symbol,Date,Open,High,Low,Close,Volume):
        stock_id = f"{Symbol}_{Date}".lower()
        formatted_date = datetime.strptime(Date, '%d-%b-%y').date().strftime('%Y-%m-%d')

        self.db.add_to_table("stock", "VALUES (?,?,?,?,?,?,?,?)", (
            stock_id,
            Symbol,
            formatted_date,
            Open,
            High,
            Low,
            Close,
            Volume
        ))

    def fetch_stocks_data_from_db(self, symbol=None):
        filter_by_stock = f'WHERE symbol="{symbol}"' if symbol else ''
        return self.db.fetchDataFromDB(f'SELECT symbol, date, open, high, low, close, volume FROM stock {filter_by_stock} ORDER BY date ASC')
