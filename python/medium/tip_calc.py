
amount =0
level = ""

while amount <= 0 :
    amount = float(input("Total bill amount? "))

while level!='good' and level!='fair' and level!='bad' :
    level = input("Level of service? ")

if level == "good" :
    tip = 20
elif level == "fair" :
    tip = 15
elif level == "bad" :
    tip = float(10)

tip_amount = amount * tip / 100
total= amount * tip / 100+amount
print("Tip amount: $%.2f" %tip_amount )
print('Total amount: $%.2f' % total )