# working code used datetime successfully - 07/09/22 @ 5:48 pm

from datetime import date

# Initiating lists
symbols = ["GOOGLE", "MSFT", "RDS-A", "AIG","FB","M","F","IBM"]
numberShares = [125,85,400,235,130,425,85,80]
pricePurchase = [772.88, 56.60, 49.58, 54.21, 124.31,30.30,12.58,150.37]
priceNow = [941.53,73.04,55.74,65.27, 175.45, 23.98,10.95,145.30]
totalNow = []
totalPurchase = []
gainLoss = []

# prints header
print(f'-'*100 + f'|')
print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Price Purchase' + "-" *5 + 'Price Now'+ "-" *5 + 'Gain/Loss'+'-'*9 + 'YoY'+'-'*13, f'|' )
print(f'-'*100 + f'|')

# Second function to calculate Gain or Loss
def calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase):
    #Calulcating Gain/Loss
    for value1, value2 in zip(priceNow,numberShares):
        totalNow.append(value1*value2)
    for value1, value2 in zip(pricePurchase,numberShares):
        totalPurchase.append(value1*value2)
    for value1, value2 in zip(totalNow,totalPurchase):
        gainLoss.append(value1-value2)

# First function: Moved code from last week in a separate function - passing positional arguments
def printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss):
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        
        # Calling calculateGainLoss function from inside the for loop
        calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase)
        
        todaysDate = date.today()
        purchaseDate = date(2017, 8, 1)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
        
        
        # prints each stock in separate lines
        print(f"|" + f"-"*7 + (f"{oneStock}") +'-' * 
                (8-len(oneStock)) + f"-"*4 + f'|{numberShares[index]}'+'-'*10 
                + '${:,.2f}'.format(pricePurchase[index]) 
                +'-'*12 
                + '${:,.2f}'.format(priceNow[index])
                +'-'*9
                + '${:,.2f}'.format(gainLoss[index])
                +'-'*10
                + f"{'{:,.2f}'.format(((gainLoss[index]/pricePurchase[index])/daysSincePurchase)*100)}%"
                +'-'*5
                + f'|') 
        
        #prints separator
        print(f'-'*93 + f'|')
        
        
# Initializing the calculateGainLoss function - passing parameters
printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss)

