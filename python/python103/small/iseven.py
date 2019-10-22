def is_even (num) :
	return num%2 == 0 

num = int (input("Please enter a number: "))
print("{} is an even number : {}".format(num, is_even(num)))

