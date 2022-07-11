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
    
        # (ln44-54)) prints each stock in separate rows in table
        print(f" " + f" "*7 + (f"{oneStock}") +' ' * 
                (8-len(oneStock)) + f" "*4 + f' {numberShares[index]}'+' '*10 
                + '${:,.2f}'.format(pricePurchase[index]) 
                +' '*12 
                + '${:,.2f}'.format(priceNow[index])
                +' '*9
                + '${:,.2f}'.format(gainLoss[index])
                +' '*10
                + f"{'{:,.2f}'.format(((gainLoss[index]/pricePurchase[index])/daysSincePurchase)*100)}%"
                +' '*5
            ) 
        
        # prints separator
        print(f'-'*93 )
        # + f'|'