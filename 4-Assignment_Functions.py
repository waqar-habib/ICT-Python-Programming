# WORKING CODE: 07/09 @ 4:26; prints table perfectly
symbols = ["A", "B", "C", "D"]
numberShares = [10,11,15,20]
pricePurchase = [40, 10, 20, 30]
priceNow = [30,25,40,15]

# Creating a function to print lists
def calculateGainLoss(symbols, numberShares, pricePurchase, priceNow):
    # Header
    print(f'-'*65 + f'|')
    print(f"|"+ '-' * 3 + 'Stock Name' + "-" *5 + 'Shares' + "-" *6 + 'Price Purchase' + "-" *5 + 'Price Now'+ "-" *5, f'|' )
    print(f'-'*65 + f'|')
    
    #for loop to loop through all stocks
    for index, oneStock in enumerate(symbols):
        currencyPP = "${:,.2f}".format(pricePurchase[index])
        currencyPN = "${:,.2f}".format(priceNow[index])
        print(f"|" + f"-"*7 + (f"{oneStock}") +'-' * 
            (8-len(oneStock)) + f"-"*4 + f'|{numberShares[index]}'+'-'*10 + f'|{currencyPP}'+'-'*11 + f'|{currencyPN}'+'-'*7+ f'|') 
        print(f'-'*65 + f'|')
        
# Initializing the calculateGainLoss function
calculateGainLoss(symbols, numberShares, pricePurchase, priceNow)


