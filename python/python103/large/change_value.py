def bills(bill):
	hundred = bill[5] *100
	fifty = bill[4] * 50
	twenty = bill[3] * 20
	ten = bill[2] * 10
	five = bill[1] * 5
	single = bill[0] * 1

	return ( single+five+ten+twenty+fifty+hundred)

def coins(coin):
	quarter = coin[3] * 25
	dimes = coin[2] * 10
	nickels = coin[1] * 5
	pennies = coin[0] * 1
	
	return (pennies + nickels + dimes + quarter)

def value_of_change(money):
	b = bills(money[0])
	c = coins(money[1])

	return ( b + (c/100))

bill = ['singles', 'fives', 'ten', 'twenty', 'fifties', 'hundred']
coin= ['pennies', 'nickel', 'dimes', 'quarters']
b=[]
c=[]
for i in bill :
	tmp  = input("How many {} do you have? ".format(i))
	while not tmp:
		tmp  = input("How many {} do you have? ".format(i))
	b.append(int(tmp))

for i in coin:
	tmp = input("How many {} do you have? ".format(i))
	while not tmp:
		tmp = input("How many {} do you have? ".format(i))
	c.append(int(tmp))

b = tuple(b)
c = tuple(c)
monetary = b,c
print(monetary)
money=float(value_of_change(monetary))
print("You have $%.2f" % money)
