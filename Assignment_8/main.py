import matplotlib.pyplot as plt
# local modules
from modules.utilities import get_JSON, get_CSV
from modules.stock import Stock
from modules.databaseManagement import Database

def dataConstruct(stocksListJSON, stocksListCSV, colors):
    stocksDictionary = {}
    for stock in reversed(stocksListJSON):
        if stock['Symbol'] not in stocksDictionary:
            numShares = stocksListCSV[stock['Symbol']]
            color = colors[stock['Symbol']]
            singleStock = Stock(stock['Symbol'], numShares, color, stock['Date'], stock['Close'])
            stocksDictionary[stock['Symbol']] = singleStock
        else:
            stocksDictionary[stock['Symbol']].createList(stock['Date'], stock['Close'])

    return stocksDictionary

def main():
    stockDataJSON = get_JSON('data/AllStocks.json')
    stocksListCSV = get_CSV('data/stocks.csv')

    databaseMgmt = Database('stocks_data.db')
    databaseMgmt.addInvestment(stockDataJSON)
    colors = {
                'GOOG':'navy', 
                'MSFT':'red', 
                'RDS-A': 'teal', 
                'AIG': 'crimson', 
                'FB': 'orangered', 
                'M':'lime', 
                'F': 'black', 
                'IBM':'yellow'
                }

    xAxis = [
                '2015-08', 
                '2015-10',
                '2016-01', 
                '2016-04', 
                '2016-07',
                '2016-10',
                '2017-01',
                '2017-04',
                '2017-07'
                ]

    # format data to simplify plotting
    stocksDictionary = dataConstruct(stockDataJSON, stocksListCSV, colors)

    # create fig, ax from subplots
    fig, ax = plt.subplots()

    # create plots from the data
    for stock in stocksDictionary.values():
        ax.plot(stock.years, stock.priceNowList, stock.color, label=stock.name)

    ax.set_xticks(xAxis)
    fig.autofmt_xdate()
    plt.legend()
    print(f"Plotting...Done")
    plt.savefig('plot.png')

    # close database connection
    databaseMgmt.close()

if __name__ == '__main__':
    main()
