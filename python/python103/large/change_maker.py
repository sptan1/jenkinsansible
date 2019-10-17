def bills(bill):
	hundred = 0
	fifty = 0
	twenty =0 
	ten =0
	five =0
	single =0

	if bill >= 100 :
		hundred = bill //100
		bill = bill %100

	if bill >= 50:
		fifty = bill // 50
		bill = bill % 50

	if bill >= 20:
		twenty = bill // 20
		bill = bill % 20

	if bill >= 10:
		ten = bill //10
		bill = bill % 10

	if bill >= 5:
		five = bill//5
		bill = bill % 5
	single = bill // 1
	bill %= 1

	return ( single, five, ten, twenty, fifty, hundred)

def coins(coin):
	quarter =0
	dimes =0 
	nickels = 0
	pennies = 0

	if coin >=25:
		quarter = coin // 25
		coin =coin % 25

	if coin >= 10:
		dimes = coin //10
		coin = coin %10
	
	if coin >= 5:
		nickels == coin //5
	
	pennies = coin //1
	coin %= 1
	
	return (pennies, nickels, dimes, quarter)

def make_change(total_charge,payment):
	c = round((payment - total_charge),2)
	print("The change is :$%.2f" % c)
	bill = int(c //1)
	coin = int(str(c).split(".")[1])
	b_tuple = bills(bill)
	c_tuple = coins(coin)
	
	return (b_tuple,c_tuple)

charge = float(input("Please enter the amount of bill: "))
pay = float(input("Please enter the payment: "))

change=make_change(charge,pay)
print(change)
print("The bills are : {} hundred, {} fifties, {} twenty, {} ten, {} fives, {} singles.".format(change[0][5],change[0][4],change[0][3],change[0][2],change[0][1],change[0][0]))
print("The coins are:  {} quarters, {} dimes, {} nickel, {} pennies".format(change[1][3],change[1][2],change[1][1],change[1][0]))
