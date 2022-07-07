#Waqar Habib

#ICT 4370
#Sat, Jul 2, 2022
#Assignment 3
 

#ln:9-14 - Converted previous lists into a dictionary   
myStocks = {
    'META': [10, 325.20, 163.74 ],
    'AAPL': [11, 319.91, 131.56 ],
    'MSFT': [15, 169.75, 247.65 ],
    'TSLA': [20, 899.94, 650.28 ],   
}
        
#ln:16-25 - Looping through each stock from portfolio and performing gain/Loss calculation for each stock from portfolio          
for symbol in myStocks:
     numShares = myStocks[symbol][0]
     pricePurchase = myStocks[symbol][1]
     priceNow = myStocks[symbol][2]
     gainLoss = numShares*priceNow - numShares*pricePurchase
     print(f"\nStock Name: {symbol}")
     print(f"Shares: {numShares}")
     currency = "${:,.2f}".format(gainLoss)
     print(f"Gain or Loss: {currency}")
  
#ln:28-32 - Conditional to print the stock with highest gain/loss
if gainLoss >= 0:
    currency = "${:,.2f}".format(gainLoss)
    print(f"\nThe highest earning stock is {symbol} with a total gain of: {currency}")
else:
    print(f"\nThe lowest earning stock is {symbol} with a total loss of: {currency}")