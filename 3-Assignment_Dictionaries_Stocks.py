#Waqar Habib

#ICT 4370
#Thu, Jun 30, 2022
#Assignment 3

#import pprint as prettyPrint


print("Part One - Dictionary")
#converting previous lists to dictionary

# pretty printing dictionary
#prettyPrint.pprint(myStocks)



myStocks = {
    'META': {
        'symbol': 'META',
        'numberShares': 10,
        'purchasePrice': 325.20,
        'priceNow': 163.74
    },
    'AAPL': {
        'symbol': 'AAPL',
        'numberShares': 11,
        'purchasePrice': 319.91,
        'priceNow': 131.56
    },
    'MSFT': {
        'symbol': 'MSFT',
        'numberShares': 15,
        'purchasePrice': 169.75,
        'priceNow': 247.65
    },
    'TSLA': {
        'symbol': 'TSLA',
        'numberShares': 20,
        'purchasePrice': 899.94,
        'priceNow': 650.28
    }
}
'''

# gaps
print("-" * 30)
print("\n" * 1)   
print("Part Two - Investor Report")
print("-" * 30)
'''
'''
for symbol, numberShares in myStocks.items():
    metaName = {symbol}
    metaShare = {numberShares}
    print(metaName)
    print(symbol)
 '''   

for symbol, singleStock in myStocks.items():
    singleStock['totalPriceAtPurchase'] = singleStock['numberShares'] * singleStock['purchasePrice']
    totalPriceAtPurchase = singleStock['totalPriceAtPurchase']
    print(f"Total price at purchase for each stock was {totalPriceAtPurchase}: ")
    
for symbol, singleStock in myStocks.items():
    singleStock['totalPricePriceNow'] = singleStock['numberShares'] * singleStock['priceNow']
    totalPricePriceNow = singleStock['totalPricePriceNow']
    print(f"Total price now for each stock is {totalPricePriceNow}: ")
    
for symbol, singleStock in myStocks.items():
    singleStock['gainLoss'] = singleStock['totalPricePriceNow'] - singleStock['totalPriceAtPurchase']
    gainLoss = singleStock['gainLoss']
    print(f"You have gained/lost: {gainLoss} on each stock")  
