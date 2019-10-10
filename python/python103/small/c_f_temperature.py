def temperature(temp):
	c = (temp * 9 / 5 ) + 32
	return c

temp = int(input("Please enter temperature in Celsius: "))
c_temp = temperature(temp)
print("The temperature {}C in Fahrenheit is : {}".format(temp, c_temp))

