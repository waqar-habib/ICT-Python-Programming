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
    
    # Method 2: Calculating Gain/Loss on EACH stock. 
    # Doing this instead of for loop from previous weeks
    def calculateGainLossOnEach(self):
        gainLossEach = round(((Stocks.calculateGainLoss(self))/(self.numberShares)),2)
        return gainLossEach
    
    # Method 3: Calculating Gain/Loss on EACH stock. 
    def calcYoYYield(self):
        totalYield = round((self.priceNow - self.pricePurchase)/(self.pricePurchase),2)
        return totalYield
    
    # Method 4: Calculating Gain/Loss on EACH stock. 
    def calcYoYRate(self):
        YoYRate = round((((self.priceNow - self.pricePurchase)/(self.pricePurchase))/Stocks.calculateDaysSince(self))*100,2)
        return YoYRate

    # Method 5: Calculating Days since purchase
    def calculateDaysSince(self):
        todaysDate = date.today()
        purchaseDate = date(self.purchaseDate)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
        return daysSincePurchase
    
    # Method 6: Printing tables 
    def printStockTables(self):
        # Prints table
        table = [[{self.symbols}],[{self.numberShares}],[Stocks.calculateGainLoss(self)],[Stocks.calcYoYYield(self)]]
        print(tabulate(table, headers=["Stock Name","Shares", "Gain/Loss","YoY"]))
        
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
    
    # Method 2: Getting year over year yield rate        
    def printBondsTable():
        # allBonds = []
        # allBonds.append(Bonds("GT2:GOV",100.02,100.05,200,1.38,1.35+"%","2017-08-01"))
        
        # print(tabulate(allBonds, headers=["Bond", "Purchase Price", "Current Price", "Quantity", "Coupon", "Total Yield","Purchase Date"]))
        bonds = []
        bonds.append(Bonds ("GT2:GOV", 200, 100.02, 100.05, "2017-08-01", 108, 1.38,.0135))
        for i in range(0, len(bonds)):
            bonds[i].printBondsTable()
    


class Investor:
    
    # Creating a special __init__ method (aka constructor)
    def __init__ (self, investorID, investorAddress, investorPhone):
        self.investorID = investorID
        self.investorAddress = investorAddress
        self.investorPhone = investorPhone
         
    def printInvestorTable(self):
        # Prints table
        table = [[{self.investorID}],[{self.investorAddress}],[{self.investorPhone}]]
        
        print(tabulate(table, headers=["Investor ID", "Investor Address", "Investor Phone"]))
    
       

Bonds.printBondsTable()

