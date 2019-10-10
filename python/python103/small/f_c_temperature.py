def temperature(temp):
	c = (temp -32) * 5 / 9
	return c

temp = int(input("Please enter temperature in Fahrenheit: "))
c_temp = temperature(temp)
print("The temperature {}F in Celsius is : {}".format(temp, c_temp))

