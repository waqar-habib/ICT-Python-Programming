def calculateGainLoss(priceNow, pricePurchase, numberShares, totalNow, totalPurchase, gainLoss):
    #Calulcating Gain/Loss
    for value1, value2 in zip(priceNow,numberShares):
        totalNow.append(value1*value2)
    for value1, value2 in zip(pricePurchase,numberShares):
        totalPurchase.append(value1*value2)
    for value1, value2 in zip(totalNow,totalPurchase):
        gainLoss.append(value1-value2)