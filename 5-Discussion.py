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
    
    
     # Calulcating Gain/Loss
    def calculateGainLoss(self):
        gainLoss = (self.priceNow - self.pricePurchase)*self.numberShares
    
        
    # Calculating Days since purchase
    def calculateDaysSince(self):
        todaysDate = date.today()
        purchaseDate = date(self.purchaseDate)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
        return daysSincePurchase
    
    