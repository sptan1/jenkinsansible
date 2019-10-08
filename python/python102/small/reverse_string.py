string = input("Enter a string: ")
new_string = ""
length = len(string) - 1
while length >= 0 :
	new_string = new_string + string[length]
	length -=1

print("The string in reversed : ", new_string)
