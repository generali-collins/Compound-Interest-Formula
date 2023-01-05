# Collins Wanga

def calculateAmount(principal,rate,time,numTimes):
    amount = principal*(1+(rate/numTimes))**(numTimes*time)
    return amount

amount = calculateAmount(1000,0.15,5,12)

print(amount)

