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
    

    #function to print the bond information
    def printBondTables (self):
        print ((str (self.symbols)), (str (self.numberShares)), ("$" + str (self.pricePurchase)), ("$" + str (self.priceNow)), (self.purchaseDate), (self.symbolID),
         (str (self.coupon)), (str (self.totalYield * 100) + "%"),sep='\t\t',end="\n")
        
#function to print the stock table header
    def stockTablesHeader():
        print("\n")
        print ("-" * 75)
        print ('\nStock \t\tShare# \t\tEarnings/Loss \tYearly Earning/Loss') 
        print ("-" * 75)
        
#function to print the stock table information
    def printStockData (self):
        print('-' *70)
        print (f"{(str (self.symbols))}\t\t{(str (self.numberShares))}\t\t{(str (Stocks.calculateGainLoss (self)))}\t\t {( (Stocks.calcYoYRate (self))):.2f}") 
        print('-' *70)


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
    print("hello")
    

class Investor:
    
    # Creating a special __init__ method (aka constructor)
    def __init__ (self, investorID, investorAddress, investorPhone):
        self.investorID = investorID
        self.investorAddress = investorAddress
        self.investorPhone = investorPhone
         
    def printInvestorHeader():
        print ("-" * 50)
        print ('investorID  \taddress \tcontactNumber')
        print ("-" * 50)

    def printInvestorTable (self):
        print (self.investorID,self.investorAddress,self.investorPhone,sep= '\t')
        
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

    
#inputting the bond information to the bond class
print('\nBond Table')
print("\n" * 1)
print(f'Bond' + " " *11 + 'Shares' + " " *6 + 'Purchased At' + " " *8 + 'Value Now'+ " " *8+ 'Date Purchased' + " " *6 + 'Quantity'+' '*10 + 'Coupon'+' '*13 + 'Yield' + " " *6)
print(f'-'*130)
bonds = []
bonds.append(Bonds ("GT2:GOV", 200, 100.02, 100.05, "2017-08-01", 108, 1.38,.0135))

# Bonds.printBondHeader()     

#calling the function to print bonds information
for i in range(len(bonds)):
    bonds[i].printBondTables()
print('\n\n')
print('*'*125)

#calling the funtion to printthe bond table header
Stocks.stockTablesHeader()

#calling the function to print stocks information
for key in stockList:
    stockList.get(key).printStockData()
print('\n\n')
print('*'*125)

#inputting the investor information to the investor class
investors = []
investors.append(Investor (1, "S Way St, Aurora, CO", "720-921-9999"))
print('\n\nInvestor Table')

#calling the funtion to printthe bond table header
Investor.printInvestorHeader()

#calling the function to print investor details
for i in range(len(investors)):
    investors[i].printInvestorTable()