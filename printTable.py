from datetime import date
from calculateGainLoss import calculateGainLoss

totalNow = []
totalPurchase = []

# First function: Moved code from last week in a separate function - passing positional arguments
def printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss):
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        
        # Calling calculateGainLoss function from inside the for loop
        calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase, gainLoss)
        
        # Calculating daysSincePurchase to plug into ln 52
        todaysDate = date.today()
        purchaseDate = date(2017, 8, 1)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
    
        # Prints each stock in separate rows in table
        print(f" " + f" "*7 + (f"{oneStock}") +' ' * 
                (8-len(oneStock)) + f" "*4 + f' {numberShares[index]}'+' '*10 
                + '${:,.2f}'.format(pricePurchase[index]) 
                +' '*15 
                + '${:,.2f}'.format(priceNow[index])
                +' '*15
                + '${:,.2f}'.format(gainLoss[index])
                +' '*15
                + f"{'{:,.2f}'.format(((gainLoss[index]/pricePurchase[index])/daysSincePurchase)*100)}%"
                +' '*15
            ) 
        
        # prints separator
        print(f'-'*110 )
