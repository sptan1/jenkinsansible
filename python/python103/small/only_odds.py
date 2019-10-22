def is_even(num):
	return num%2 == 0

def is_odd(num):
        return (not is_even(num))

def only_odds(list) :
	list2 = []
	for i in list :
		if is_odd(i) :
			list2.append(i)
	return list2

list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

print("The list is: {}".format(list))
print("The odd numbers in the list are : ", end="")
print(only_odds(list))
