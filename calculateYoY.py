from datetime import date

# Third function to calculate year over year yield    
def calculateYoY (symbols, gainLoss, pricePurchase):
            
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