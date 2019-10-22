def is_even(num):
	return num%2 == 0

def only_evens(list) :
	list2 = []
	for i in list :
		if is_even(i) :
			list2.append(i)
	return list2

list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

print("The list is: {}".format(list))
print("The even numbers in the list are : ", end="")
print(only_evens(list))
