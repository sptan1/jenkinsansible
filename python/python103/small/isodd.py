def is_even (num) :
	return num%2 == 0 

def is_odd(num):
	return (not is_even(num))

num = int (input("Please enter a number: "))
print("{} is an odd number : {}".format(num, is_odd(num)))

