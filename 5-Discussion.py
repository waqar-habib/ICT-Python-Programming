from datetime import date

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
    
    # Method: 3 Calculating Days since purchase
    def calculateDaysSince(self):
        todaysDate = date.today()
        purchaseDate = date(self.purchaseDate)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
        return daysSincePurchase
    
    