
from datetime import date
from datetime import timedelta

# Initiating lists
symbols = ["A", "B", "C", "D"]
numberShares = [10,11,15,20]
pricePurchase = [40, 10, 20, 30]
priceNow = [30,25,40,15]
totalNow = []
totalPurchase = []
gainLoss = []

# prints header
print(f'-'*79 + f'|')
print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Price Purchase' + "-" *5 + 'Price Now'+ "-" *5 + 'Gain/Loss'+'-'*5, f'|' )
print(f'-'*79 + f'|')

# Creating a function to print lists - passing positional arguments
def printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss):
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        
        #Calulcating Gain/Loss
        for value1, value2 in zip(priceNow,numberShares):
            totalNow.append(value1*value2)

        for value1, value2 in zip(pricePurchase,numberShares):
            totalPurchase.append(value1*value2)
    
        for value1, value2 in zip(totalNow,totalPurchase):
            gainLoss.append(value1-value2)
        
        # prints each stock in separate lines
        print(f"|" + f"-"*7 + (f"{oneStock}") +'-' * 
            (8-len(oneStock)) + f"-"*4 + f'|{numberShares[index]}'+'-'*10 
            + '${:,.2f}'.format(pricePurchase[index]) 
            +'-'*11 
            + '${:,.2f}'.format(priceNow[index])
            +'-'*8 
            + '${:,.2f}'.format(gainLoss[index])
            +'-'*8 
            + f'|') 
        
        #prints separator
        print(f'-'*79 + f'|')
        
        # def calcYoY(gainLoss,pricePurchase):
        #     currentDate = date.today()
        #     purchaseDate = currentDate - timedelta(days = 1801)
            
        #     print(
        #         ((gainLoss[index]/pricePurchase[index]))
        #     )
        
        # calcYoY(gainLoss,priceNow)
        
        

# Initializing the calculateGainLoss function - passing parameters
printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss)

print('*'*100)
print("YoY Calculation")
print('*'*100)

# Get today's date
currentDate = date.today()
print("Today is: ", currentDate)
 
# Yesterday date
purchaseDate = currentDate - timedelta(days = 1801)
print("Purchase Date was: ", purchaseDate)

