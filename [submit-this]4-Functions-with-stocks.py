# working code added calculate YoY function to print statements under the table - 07/09/22 @ 11:47 pm

from datetime import date

# Initiating lists
symbols = ["GOOGLE", "MSFT", "RDS-A", "AIG","FB","M","F","IBM"]
numberShares = [125,85,400,235,130,425,85,80]
pricePurchase = [772.88, 56.60, 49.58, 54.21, 124.31,30.30,12.58,150.37]
priceNow = [941.53,73.04,55.74,65.27, 175.45, 23.98,10.95,145.30]
totalNow = []
totalPurchase = []
gainLoss = []

# (ln 15-17) prints table header
print(f'-'*100 + f'|')
print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Price Purchase' + "-" *5 + 'Price Now'+ "-" *5 + 'Gain/Loss'+'-'*9 + 'YoY'+'-'*13, f'|' )
print(f'-'*100 + f'|')

# (ln 20-27/needs refactoring) Second function to calculate Gain or Loss
def calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase):
    #Calulcating Gain/Loss
    for value1, value2 in zip(priceNow,numberShares):
        totalNow.append(value1*value2)
    for value1, value2 in zip(pricePurchase,numberShares):
        totalPurchase.append(value1*value2)
    for value1, value2 in zip(totalNow,totalPurchase):
        gainLoss.append(value1-value2)
        
# (ln 30-59) First function: Moved code from last week in a separate function - passing positional arguments
def printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss):
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        
        # Calling calculateGainLoss function from inside the for loop
        calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase)
        
        # Calculating daysSincePurchase to plug into ln 52
        todaysDate = date.today()
        purchaseDate = date(2017, 8, 1)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
    
        # (ln44-54)) prints each stock in separate rows in table
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
        
        # prints separator
        print(f'-'*93 + f'|')
        
# Initializing the calculateGainLoss function - passing parameters
printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss)

# Third function to calculate year over year yield    
def calculateYoY (symbols, gainLoss, pricePurchase):
       
        # (ln 65-67) Had to repeat daysSincePurchase code because couldn't figure out how to call it in printTable function in line 38-41 :(
            
        todaysDate = date.today()
        purchaseDate = date(2017, 8, 1)
        daysSincePurchase = ((todaysDate-purchaseDate).days)/365
        
        # (ln 72-77) Loop through stocks & calculate % yield  
        for j in range(0, len(symbols)):
            YoY = ((gainLoss[j]/pricePurchase[j])/daysSincePurchase)*100
            if YoY >= 0:
                print(f"You gained {'{:,.2f}'.format(YoY)}% on your {symbols[j]} stock")
            else:
                print(f"You lost {'{:,.2f}'.format(YoY)}% on your {symbols[j]} stock")
    
calculateYoY(symbols, gainLoss, pricePurchase)


'''
Note to self: 
You created a new function calculateYoY (63-79) to print 8 statements based on if you gained/lost x% on each stock. 
to Do:
1. Fix formatting
2. move funtions to modules
3. refactor 2nd function calculateGainLoss
4. Purchase date for stocks M,F,IBM is 3 different new ones. All older ones is 8/1/2017
5. See if you have to include dictionaries...

'''

