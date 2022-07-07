#Waqar Habib

#ICT 4370
#Wed, Jul 7, 2022
#Assignment 4

# 1. Move the code used to calculate the loss/gain to a function. Execute it. 

# Initiating Lists
# symbols = ["META", "AAPL", "MSFT", "TSLA"]
# numberShares = [10,11,15,20]
# pricePurchase = [325.20, 319.91, 169.75,899.94]
# priceNow = [163.74,131.56,247.65,650.28]
# totalNow = []
# totalPurchase = []
# gainLoss = []


symbols = ["A", "B", "C", "D"]
numberShares = [10,11,15,20]
pricePurchase = [40, 10, 20, 30]
priceNow = [30,25,40,15]

# Creating a function to print lists
def calculateGainLoss(symbols, numberShares, pricePurchase, priceNow):
    # Header
    print(f'-'*45 + f'|')
    print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Gain/Loss' + "-" *5 + f'|' )
    print(f'-'*45 + f'|')
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        currency = "${:,.2f}".format(pricePurchase[index], priceNow[index])
        print((f'|{oneStock.title().upper()}') +'-' * 
            (5-len(oneStock)) + f'|{numberShares[index]}'+'-'*10 + f'|{currency}'+'-'*6 + f'|{currency}'+'-'*6+ f'|') 
        print(f'-'*45 + f'|')
        
# Initializing the calculateGainLoss function
calculateGainLoss(symbols, numberShares, pricePurchase, priceNow)


'''
print("Part Two - Investor Report")
print("-" * 30)

#Calulcating Gain/Loss)
for value1, value2 in zip(priceNow,numberShares):
    totalNow.append(value1*value2)

for value1, value2 in zip(pricePurchase,numberShares):
    totalPurchase.append(value1*value2)
    
for value1, value2 in zip(totalNow,totalPurchase):
    gainLoss.append(value1-value2) 
        
  
print('\n Stock Ownership for John:')

# Format each stock symbol, no. shares and their and corresponding gain/loss:
# Prof: I know it's a lot of lines, but I just wanted to separate them for my sanity

print(f'-'*45 + f'|')
print(f"|"+ 
      '-' * 3 + 
      'Stock Name' + 
      "-" *5 + 
      'Shares' +
      "-" *6 + 
      'Gain/Loss' + 
      "-" *5 + f'|' )
print(f'-'*45 + f'|')

#for loop to loop through all stocks
for index, oneStock in enumerate(symbols):
    currency = "${:,.2f}".format(gainLoss[index])
    print((f'|{oneStock.title().upper()}') +'-' * 
          (18-len(oneStock)) + f'|{numberShares[index]}'+'-'*6 + f'|{currency}'+'-'*6 + f'|')
    print(f'-'*45 + f'|')

#For loop to print each in a separate line
index = 0
for x in symbols:
    spacesRow = 12-len(symbols[index])
    name = symbols[index]
    weight = {gainLoss[index]}
    index += 1


#ln85-105 calculation for the highest/lowest value stock symbols/gain or loss
highestValue = max(gainLoss)
highestSymbol = max(symbols)

lowestValue = min(gainLoss)
lowestSymbol = min(symbols)

print("\n" * 1)

if highestValue >= 0:
    print(f"The highest earning stock is: {highestSymbol} with a loss of:")
    print("${:,.2f}".format(highestValue))
else:
    print(f"The lowest earning stock is: {lowestSymbol} with a loss of:")
    print("${:,.2f}".format(lowestValue))

if lowestValue >= 0:
    print(f"The highest earning stock is: {highestSymbol} with a loss of:")
    print("${:,.2f}".format(highestValue))
else:
    print(f"The lowest earning stock is: {lowestSymbol} with a loss of:")
    print("${:,.2f}".format(lowestValue))
  
    print("\n" * 1)
    
'''
# Extra formatting code

# Part One 
# print("\n" * 1)
# print("Part One - Stock Price List")
# print("-" * 30)