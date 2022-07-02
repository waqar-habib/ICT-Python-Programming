#Dictionary of Portfolio

myStocks = {
    # each list is called "listOfData" in ln14-17
    # item in each is called "data" in ln14-17
    'META': [10, 325.20, 163.74 ],
    'AAPL': [11, 319.91, 131.56 ],
    'MSFT': [15, 169.75, 247.65 ],
    'TSLA': [20, 899.94, 650.28 ],   
}

#for loop

for symbol, listOfData in myStocks.items():
    print(f"\n{symbol}")
    for data in listOfData:
        print(f"{data}")
        
# uncomment the following for Gain/Loss   
for symbol in myStocks:
     numShares = myStocks[symbol][0]
     pricePurchase = myStocks[symbol][1]
     priceNow = myStocks[symbol][2]
     gainLoss = numShares*priceNow -      numShares*pricePurchase
     print(f"Total Gain or Loss on {symbol} stock: {gainLoss}")


gainLoss = numShares*priceNow -      numShares*pricePurchase
print(f"hello {gainLoss}")