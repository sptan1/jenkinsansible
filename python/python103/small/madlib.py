def madlib(name, subject):
	string = "# \"{}'s favorite subject is {}.\"".format(name,subject)
	return (string)


name = input("Please enter a name: ")
subject = input ("Please enter a subject: ")

if name == "" :
	name = "ShuPei"
if subject == "" :
	subject = "math"

result = madlib(name,subject)
print("madlib(\"{}\", \"{}\")".format(name,subject))
print(result)


