from datetime import date
from pandas import *

# class Stocks:
#     def __init__(self,symbols,numberShares, pricePurchase,priceNow, purchaseDate1, purchaseDate2, symbolID ):
#         self.symbols = symbols
#         self.numberShares = numberShares
#         self.pricePurchase = pricePurchase
#         self.priceNow = priceNow
#         # purchaseDate1 = GOOG, MSFT,RDSA, AIG, FB
#         self.purchaseDate1 = purchaseDate1
#         #  purchaseDate2 = M, F, IBM
#         self.purchaseDate2 = purchaseDate2
#         self.symbolID = symbolID





# ---------- STOCKS ----------
try:
    stockFile = 'ICT-Python-Programming/ICT-Python-Programming/6-stocks.csv'

    # feeding data through stock file
    dataStocks = read_csv(stockFile)

    # converting column data to list
    symbols = dataStocks['SYMBOL'].tolist()
    numberShares = dataStocks['NO_SHARES'].tolist()
    pricePurchase = dataStocks['PURCHASE_PRICE'].tolist()
    priceNow = dataStocks['CURRENT_VALUE'].tolist()
    purchaseDate = dataStocks['PURCHASE_DATE'].tolist()

    # printing list data
    print('Stocks')
    print('Symbols:', symbols)
    print('Shares:', numberShares)
    print('Purchase Price:', pricePurchase)
    print('Current Price:', priceNow)
    print('Purchase Date:', purchaseDate)

except FileNotFoundError:
    print("")
    print("The file "+ stockFile + " does not exist. Please check the file path and try again.")
    print("")

# -------- BONDS -------
# feeding data through bond file
try:
    bondFile = 'ICT-Python-Programming/ICT-Python-Programming/6-bonds.csv'

    # feeding data through bond file
    dataBonds = read_csv(bondFile)

    # converting column data to list
    symbols = dataBonds['SYMBOL'].tolist()
    numberShares = dataBonds['NO_SHARES'].tolist()
    pricePurchase = dataBonds['PURCHASE_PRICE'].tolist()
    priceNow = dataBonds['CURRENT_VALUE'].tolist()
    bondPurchaseDate = dataBonds['PURCHASE_DATE'].tolist()
    coupon = dataBonds['Coupon'].tolist()
    bondYield = dataBonds['Yield'].tolist()

    # printing list data
    print("Bonds")
    print('Symbols:', symbols)
    print('Shares:', numberShares)
    print('Purchase Price:', pricePurchase)
    print('Current Price:', priceNow)
    print('Purchase Date:', bondPurchaseDate)
    print('Coupon:', coupon)
    print('Yield:', bondYield)

except FileNotFoundError:
    print("")
    print("The file "+ bondFile + " does not exist. Please check the file path and try again.")
    print("")