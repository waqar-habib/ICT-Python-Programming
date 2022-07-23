from datetime import date
from pandas import *
import numpy as np

class Stocks:
    def __init__(self,symbols,numberShares, pricePurchase,priceNow, purchaseDate, symbolID ):
        self.symbols = symbols
        self.numberShares = numberShares
        self.pricePurchase = pricePurchase
        self.priceNow = priceNow
        self.purchaseDate = purchaseDate
        self.symbolID = symbolID
        
    # Method 1: Calulcating Gain/Loss on all Stocks
    def calculateGainLoss(self):
        gainLoss = round(((self.priceNow - self.pricePurchase)*self.numberShares),2)
        return gainLoss
        
       
  


# ---------- STOCKS ----------
try:
    stockFile = 'ICT-Python-Programming/ICT-Python-Programming/6-stocks.csv'

    # feeding data through stock file
    dataStocks = read_csv(stockFile)

    # converting column data to list
    symbolID = dataStocks['SYMBOL_ID'].tolist()
    symbols = dataStocks['SYMBOL'].tolist()
    numberShares = dataStocks['NO_SHARES'].tolist()
    pricePurchase = dataStocks['PURCHASE_PRICE'].tolist()
    priceNow = dataStocks['CURRENT_VALUE'].tolist()
    purchaseDate = dataStocks['PURCHASE_DATE'].tolist()

    print(symbols)
    
    array1 = np.array1(numberShares)
    array2 = np.array2(priceNow)
    array2 = np.array2(pricePurchase)
    
    # myStock = Stocks(symbols, numberShares, pricePurchase, priceNow, purchaseDate, symbolID)
    # myStock.calculateGainLoss()
    # print(myStock.calculateGainLoss())  
    
    # # printing list data
    # print('Stocks')
    # print('Symbols:', symbols)
    # print('Shares:', numberShares)
    # print('Purchase Price:', pricePurchase)
    # print('Current Price:', priceNow)
    # print('Purchase Date:', purchaseDate)

except FileNotFoundError:
    print("")
    print(stockFile + " not found")
    print("")
    
# print(dataStocks)

# -------- BONDS -------
# feeding data through bond file
try:
    bondFile = 'ICT-Python-Programming/ICT-Python-Programming/6-bonds.csv'

    # feeding data through bond file
    dataBonds = read_csv(bondFile)

    # converting column data to list
    # symbols = dataBonds['SYMBOL'].tolist()
    # numberShares = dataBonds['NO_SHARES'].tolist()
    # pricePurchase = dataBonds['PURCHASE_PRICE'].tolist()
    # priceNow = dataBonds['CURRENT_VALUE'].tolist()
    # bondPurchaseDate = dataBonds['PURCHASE_DATE'].tolist()
    # coupon = dataBonds['Coupon'].tolist()
    # bondYield = dataBonds['Yield'].tolist()

    # # printing list data
    # print("Bonds")
    # print('Symbols:', symbols)
    # print('Shares:', numberShares)
    # print('Purchase Price:', pricePurchase)
    # print('Current Price:', priceNow)
    # print('Purchase Date:', bondPurchaseDate)
    # print('Coupon:', coupon)
    # print('Yield:', bondYield)

except FileNotFoundError:
    print("")
    print(bondFile + " not found")
    print("")

# print('\n',dataBonds)