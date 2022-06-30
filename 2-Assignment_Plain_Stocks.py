
print("\n" * 1)
print("Part One - Stock Price List")
print("-" * 30)

symbols = ["META", "AAPL", "MSFT", "TSLA"]
numberShares = [10,11,15,20]
pricePurchase = [325.20, 319.91, 169.75,899.94]
priceNow = [163.74,131.56,247.65,650.28]
totalNow = []
totalPurchase = []
gainLoss = []

print("Stock Symbols"); print(symbols)
print("\n" * 1)
print("Number of Shares"); print(numberShares)
print("\n" * 1)
print("Purchase Price"); print(pricePurchase)
print("\n" * 1)
print("Current Price"); print(priceNow)

'''
# Prof: I had already used pandas on the first so I'll just leave it here...
# convert the list into dataframe row by
# using zip()
data = pd.DataFrame(list(zip(symbols, numberShares, pricePurchase, priceNow)),
                    columns=['Stock Symbol', 'No. Shares', 'Purchase Price','Current Value'])

print(data)
'''

print("-" * 30)
print("\n" * 1)


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
    
