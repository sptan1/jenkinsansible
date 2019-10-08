amount =0
level = ""
split =0

while amount <= 0 :
    amount = float(input("Total bill amount? "))

while level!='good' and level!='fair' and level!='bad' :
    level = input("Level of service? ")

while split <= 0 :
    split=int(input("Split how many ways? "))

if level == "good" :
    tip = 20
elif level == "fair" :
    tip = 15
elif level == "bad" :
    tip = float(10)

tip_amount = amount * tip / 100
total= tip_amount + amount
split_amount = total / split
print("Tip amount: $%.2f" %tip_amount )
print('Total amount: $%.2f' % total )
print('Amount per person: $%.2f' % split_amount)