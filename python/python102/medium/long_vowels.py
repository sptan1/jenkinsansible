string = input("Please enter a string: ")
l_str = list(string)
length = len(string)

for i in range(length) :
	if l_str[i] == l_str[i-1] :
		l_str[i] = l_str[i]*4

new_str = "".join(l_str)
print("{} => {}".format(string, new_str))

