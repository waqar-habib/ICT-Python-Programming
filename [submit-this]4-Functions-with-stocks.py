# working code added calculate YoY function to print statements under the table - 07/09/22 @ 11:47 pm

from datetime import date
from calculateGainLoss import calculateGainLoss
from calculateYoY import calculateYoY
from printTable import printTable

# Initiating lists
symbols = ["GOOGLE", "MSFT", "RDS-A", "AIG","FB","M","F","IBM"]
numberShares = [125,85,400,235,130,425,85,80]
pricePurchase = [772.88, 56.60, 49.58, 54.21, 124.31,30.30,12.58,150.37]
priceNow = [941.53,73.04,55.74,65.27, 175.45, 23.98,10.95,145.30]
totalNow = []
totalPurchase = []
gainLoss = []

# Prints table header
print("\n" * 1)
print(f" "+ ' ' * 3 + 'Stock Name' + " " *5 + 'Shares' + " " *6 + 'Price Purchase' + " " *8 + 'Price Now'+ " " *16 + 'Gain/Loss'+' '*16 + 'YoY'+' '*13 )
print(f'-'*110)
       
# Calling printTable as a module
printTable(symbols, numberShares, pricePurchase, priceNow, gainLoss)

# Calling calculateYoY as a module
calculateYoY(symbols, gainLoss, pricePurchase)


