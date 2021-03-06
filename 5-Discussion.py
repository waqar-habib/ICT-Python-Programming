#Waqar Habib

#ICT 4370
#Wed, Jul 13, 2022
#Discussion 5

from datetime import date
from tabulate import tabulate

# Creating a class named Stocks
class Stocks:
    # Creating a special __init__ method (aka constructor)
    def __init__(self,symbols,numberShares,pricePurchase,priceNow,purchaseDate, symbolID):
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
    
    # Method 2: Calculating Gain/Loss on EACH share. 
    def calculateGainLossOnEachShare (self):
        gainLossEachShare = round([(Stocks.calculateGainLoss(self))/(self.numberShares)],2)
        return gainLossEachShare
    
    # Method 3: Calculating Gain/Loss on EACH stock. 
    def calcYoYYield(self):
        totalYield = round((self.priceNow - self.pricePurchase)/(self.pricePurchase),2)
        return totalYield
    
    # Method 4: Calculating Year over year %. 
    def calcYoYRate(self):
        YoYRate = round((((self.priceNow - self.pricePurchase)/(self.pricePurchase))/Stocks.calculateDaysSince(self))*100,2)
        return YoYRate
    
    # Method 5: Calculating Days since purchase
    def calculateDaysSince(self):
        todaysDate = date.today ()
        purchaseDate = self.purchaseDate 
        formattedPurchaseDate = date.fromisoformat (purchaseDate) 
        daysSincePurchase = ((todaysDate - formattedPurchaseDate).days)/365
        return daysSincePurchase
    
    # Printing Bond Table
    def printBondTables (self):
        print(tabulate({"Bond": [(str (self.symbols))],
                        "Shares": [(str (self.numberShares))],
                        "Purchased At":[("$" + str (self.pricePurchase))],
                        "Value Now":[("$" + str (self.priceNow))],
                        "Date":[(self.purchaseDate)],
                        "Quantity":[(self.symbolID)],
                        "Coupon":[(str (self.coupon))],
                        "Yield":[((str (self.totalYield * 100) + "%"))]}
                       ,tablefmt="pretty"))
    
        
    # Printing Stock Table
    def printStockTable (self):    
        print(tabulate({"Symbols": [self.symbols],
                        "Shares": [self.numberShares],
                        "Gain/Loss":[(Stocks.calculateGainLoss (self))],
                        "YoY":[(Stocks.calcYoYRate (self))]}
                       ,tablefmt="pretty"))


# Creating a new class named Bonds and passing in class Stocks
class Bonds(Stocks):
    
    # Creating a special __init__ method (aka constructor)
    def __init__ (self, stockName, stockShares, purchasePrice, currentPrice, datePurchase, symbolID, stockCoupon, totalYield):
        
        # Inherits from class Stocks
        super ().__init__ (stockName, stockShares, purchasePrice, currentPrice, datePurchase, symbolID)
        self.coupon = stockCoupon
        self.totalYield = totalYield
    
    # Method 1: Getting Coupons
    def get_Coupons(self):
        return self.coupon
    
    # Method 2: Getting year over year yield rate        
    def get_YoYRate(self):
        return self.totalYield

class Investor:
    
    # Creating a special __init__ method (aka constructor)
    def __init__ (self, investorID, investorAddress, investorPhone):
        self.investorID = investorID
        self.investorAddress = investorAddress
        self.investorPhone = investorPhone
    
    # Creating a method to print Investor table     
    def printInvestorTable (self):
        print(f'-'*43)
        print(f" "*1+'ID' + " " *8 + 'Address' + " " *12 + 'Phone')
        print(tabulate({"ID": [self.investorID],
                        "Address": [self.investorAddress],
                        "Phone":[self.investorPhone]}
                       ,tablefmt="pretty"))
        
      

    
#inputting the bond information to the bond class
print('\nBond Table')
print("-" * 70)
print(f" "*3+'Bond' + " " *3 + 'Shares' + " " *2 + 'Purchase' + " " *2 + 'Value Now'+ " " *4+ 'Date' + " " *6 + 'Qty.'+' '*2 + 'Coupon'+' '*2 + 'Yield' + " " *2)
bonds = []
bonds.append(Bonds ("GT2:GOV", 200, 100.02, 100.05, "2017-08-01", 108, 1.38,.0135))   

#calling the function to print bonds information
for i in range(len(bonds)):
    bonds[i].printBondTables()
print('\n\n')

# Stock Table Header
print('Stock Table')
print("-" * 40)
print(f'Stock' + " " *3 + 'Shares' + " " *3 + 'Gain/Loss' + " " *3 + 'Yield')

# List of all stocks
stockList= {}
stockList['GOOGLE'] = (Stocks ("GOOGLE", 125, 772.88, 941.53, "2017-08-01", 1))
stockList['MSFT'] = (Stocks ("MSFT", 85, 56.60, 73.04, "2017-08-01", 2))
stockList['RDSA'] = (Stocks ("RDSA", 400, 49.58, 55.74, "2017-08-01", 3))
stockList['AIG'] = (Stocks ("AIG", 235, 54.21, 65.27, "2017-08-01", 4))
stockList['FB'] = (Stocks ("FB", 130, 124.31, 175.45, "2017-08-01", 5))
stockList['M'] = (Stocks ("M", 425, 30.30, 23.98, "2018-01-10", 6))
stockList['F'] = (Stocks ("F", 85, 12.58, 10.95, "2018-02-17", 7))
stockList['IBM'] = (Stocks ("IBM", 80, 150.37, 145.30, "2018-05-12", 8))  

# Printing Stock Table
for key in stockList:
    stockList.get(key).printStockTable()
print('\n\n')

# Data for investor table
investors = []
investors.append(Investor (1, "S Way St, Aurora, CO", "720-921-9999"))
print('Investor Table')

# For loop for investor details
for i in range(len(investors)):
    investors[i].printInvestorTable()