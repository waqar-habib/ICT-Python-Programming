class Stocks:
    def __init__(self, symbols,numberShares, pricePurchase,priceNow, purchaseDate):
        self.symbols = symbols
        self.numberShares = numberShares
        self.pricePurchase = pricePurchase
        self.priceNow = priceNow
        self.purchaseDate = purchaseDate

    # Trying to use this method to do the following math, but since my data is in lists, this method won't run. 
    def calculateGainLoss(self):
        gainLoss = round(((self.priceNow - self.pricePurchase)*self.numberShares),2)
        return gainLoss
    
# File name as a var that can be called in the with open function
stockFile = 'ICT-Python-Programming/ICT-Python-Programming/6-stocks.csv'

# Empty Lists to append data from csv file
symbols = []
numberShares = []
pricePurchase = [] 
priceNow = []
purchaseDate = [] 
 
# Error Handling
try:
    # with open reads file and 
    with open(stockFile) as stockTable:
        # Skipping the first line in the stockTable
        next(stockTable)
        # Using "," as a delimiter to separate dog names and dog weights
        for line in stockTable:
            delimiter = line.split(',')
            # Stripping empty spaces using rstrip function
            symbols.append(delimiter[0].rstrip('\n'))
            numberShares.append(delimiter[1].rstrip('\n'))
            pricePurchase.append(delimiter[2].rstrip('\n'))
            priceNow.append(delimiter[3].rstrip('\n'))
            purchaseDate.append(delimiter[4].rstrip('\n'))
    
except FileNotFoundError:
    print("")
    print(stockFile + " not found")
    print("")  
 
# stockList = Stocks(symbols,numberShares, pricePurchase,priceNow, purchaseDate)

stockList = Stocks('GOOGL',125,772.88,941.53,'8/1/15')

print(stockList.calculateGainLoss())
