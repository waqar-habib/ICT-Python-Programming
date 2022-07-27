#Waqar Habib

#ICT 4370
#Tues, Jul 26, 2022
#Discussion 6

from datetime import datetime
from tabulate import tabulate
import sys

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
        
        
# attempt to write to file
def exportData(filepath, data):
    try:
        txt = open(filepath, "w+")
        txt.write(data)
        txt.close()

        print(f'\033[92m Summary successfully created {filepath}. \033[0m')
        
    except OSError as error:
        sys.exit(f'\n{error}.')
 
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
    
    # Printing Stock Table
    def printStockTable (self):    
        return tabulate({"Symbols": [self.symbols],
                        "Shares": [self.numberShares],
                        "Gain/Loss":[(Stocks.calculateGainLoss (self))],
                        "YoY":[(Stocks.calcYoYRate (self))]}
                       ,tablefmt="pretty")

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
    
    # Printing Bond Table
    def printBondTable (self):
        return tabulate({"Bond": [(str (self.symbols))],
                        "Shares": [(str (self.numberShares))],
                        "Purchased At":[("$" + str (self.pricePurchase))],
                        "Value Now":[("$" + str (self.priceNow))],
                        "Date":[(self.purchaseDate)],
                        "Coupon":[(str (self.coupon))],
                        "Yield":[((str (self.totalYield) + "%"))]}
                       ,tablefmt="pretty")


class Investor:
    # Creating a special __init__ method (aka constructor)
    def __init__ (self, investorID, investorAddress, investorPhone):
        self.investorID = investorID
        self.investorAddress = investorAddress
        self.investorPhone = investorPhone
    
    # Creating a method to print Investor table     
    def printInvestorTable (self):
        return f'{"-"*43}\n  ID {" " *8} Address {" " *12} Phone \n {tabulate({"ID": [self.investorID], "Address": [self.investorAddress], "Phone":[self.investorPhone]} ,tablefmt="pretty")}'
              
# Data for investor table
investors = []
investors.append(Investor (1, "S Way St, Aurora, CO", "720-921-9999"))
# print('Investor Table')

# For loop for investor details
investorTable = investors[0].printInvestorTable()
    

# Stock Table Header
stockTableHeader = f"""
Stock Table
{"-" * 40}
{f'Stock' + " " *3 + 'Shares' + " " *3 + 'Gain/Loss' + " " *3 + 'Yield'}
"""

# List of all stocks
stockList= {}

# File name as a var that can be called in the with open function
getInputFromCsv('6-stocks.csv', Stocks, stockList)

# Printing Stock Table
stockRows = '\n'.join([stockList.get(key).printStockTable() for key in stockList])
    
bondsList = {}

# File name as a var that can be called in the with open function
getInputFromCsv('6-bonds.csv', Bonds, bondsList)

#inputting the bond information to the bond class
bondsHeader = f"""
Bond Table
{"-" * 70}
{f" "*3+'Bond' + " " *3 + 'Shares' + " " *2 + 'Purchase' + " " *2 + 'Value Now'+ " " *4+ 'Date' + " " *6 + 'Coupon'+' '*2 + 'Yield' + " " *2}
"""

# Printing Bonds Table
bondsRows = '\n'.join([bondsList.get(key).printBondTable() for key in bondsList])
    
exportData('investorData.txt', f'{investorTable}\n{bondsHeader} \n{bondsRows} \n{stockTableHeader} \n{stockRows}')
