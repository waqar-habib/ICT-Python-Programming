#Waqar Habib

#ICT 4370
#Wed, Jul 13, 2022
#Discussion 6

from datetime import datetime
from tabulate import tabulate

def getInputFromCsv(filepath, InvestmentClass, investmentListDict):
    # Error Handling
    try:
        # with open reads file and 
        with open(filepath) as stockTable:
            # Skipping the first line in the stockTable
            next(stockTable)
            for line in stockTable:
                delimiter = line.split(',')
                investmentListDict[delimiter[0]] = (InvestmentClass(*delimiter)) #spread operator - spread value into multiple params
               

    except FileNotFoundError:
        print("")
        print(filepath + " not found")
        print("")  
 
# Creating a class named Stocks
class Stocks:
    # Creating a special __init__ method (aka constructor)
    def __init__(self,symbols,numberShares,pricePurchase,priceNow,purchaseDate):
        self.symbols = symbols.upper()
        self.numberShares = float(numberShares)
        self.pricePurchase = float(pricePurchase)
        self.priceNow = float(priceNow)
        self.purchaseDate = datetime.strptime(purchaseDate.rstrip('\n'), "%m/%d/%Y").date()
        # create a unique identifier for each row
        self.symbolID = f"{symbols.lower()}_{self.purchaseDate}" 
        
        
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
        todaysDate = datetime.today().date()
        daysSincePurchase = (((todaysDate - self.purchaseDate).days)/365)
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
    def __init__ (self, stockName, stockShares, purchasePrice, currentPrice, datePurchase, stockCoupon, totalYield):
        
        # Inherits from class Stocks
        super ().__init__ (stockName, stockShares, purchasePrice, currentPrice, f"{datePurchase}\n")
        self.coupon = stockCoupon
        self.totalYield = totalYield.rstrip('\n')
    
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
        
      
# Data for investor table
investors = []
investors.append(Investor (1, "S Way St, Aurora, CO", "720-921-9999"))
# print('Investor Table')

# For loop for investor details
for i in range(len(investors)):
    investors[i].printInvestorTable()
    

# Stock Table Header
print('Stock Table')
print("-" * 40)
print(f'Stock' + " " *3 + 'Shares' + " " *3 + 'Gain/Loss' + " " *3 + 'Yield')

# List of all stocks
stockList= {}

# File name as a var that can be called in the with open function
getInputFromCsv('ICT-Python-Programming/ICT-Python-Programming/6-stocks.csv', Stocks, stockList)

# Printing Stock Table
for key in stockList:
    stockList.get(key).printStockTable()
    
bondsList = {}

# File name as a var that can be called in the with open function
getInputFromCsv('ICT-Python-Programming/ICT-Python-Programming/6-bonds.csv', Bonds, bondsList)

#inputting the bond information to the bond class
bondsHeader = (f" "*3+'Bond' + " " *3 + 'Shares' + " " *2 + 'Purchase' + " " *2 + 'Value Now'+ " " *4+ 'Date' + " " *6 + 'Qty.'+' '*2 + 'Coupon'+' '*2 + 'Yield' + " " *2)

header = f"""
Bond Table
{"-" * 70}
{bondsHeader}
"""  
print(header)
# Printing Stock Table
for key in bondsList:
    bondsList.get(key).printStockTable()
    


