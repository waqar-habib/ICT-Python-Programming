

# Initiating lists
symbols = ["A", "B", "C", "D"]
numberShares = [10,11,15,20]
pricePurchase = [40, 10, 20, 30]
priceNow = [30,25,40,15]
totalNow = []
totalPurchase = []
gainLoss = []

# Creating a function to print lists - passing positional arguments
def printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss):
    
    # prints header
    print(f'-'*79 + f'|')
    print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Price Purchase' + "-" *5 + 'Price Now'+ "-" *5 + 'Gain/Loss'+'-'*5, f'|' )
    print(f'-'*79 + f'|')
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        
        # formats pricePurchase, priceNow in $
        currency = "${:,.2f}".format(pricePurchase[index], priceNow[index], gainLoss)
        
        # prints each stock in separate lines
        print(f"|" + f"-"*7 + (f"{oneStock}") +'-' * 
            (8-len(oneStock)) + f"-"*4 + f'|{numberShares[index]}'+'-'*10 + f'|{currency}'+'-'*11 + f'|{currency}'+'-'*7 + f'|{currency}'+'-'*7 + f'|') 
        
        #prints separator
        print(f'-'*79 + f'|')
        
#Calulcating Gain/Loss
    for value1, value2 in zip(priceNow,numberShares):
            totalNow.append(value1*value2)

    for value1, value2 in zip(pricePurchase,numberShares):
            totalPurchase.append(value1*value2)
    
    for value1, value2 in zip(totalNow,totalPurchase):
            gainLoss.append(value1-value2)
        
        
# Initializing the calculateGainLoss function - passing parameters
printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss)
