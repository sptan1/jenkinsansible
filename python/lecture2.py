# class Greeting :
#     def __init__(self,name, city):         #constructor -> everytime this class is call, this will be run
#         #print("I am a new object")
#         self.name = name
#         self.city = city  

#     def say_hello(self,name):
#         print("Hello World",name,self.name, self.city)

# #person1 = Greeting()
# #person1.say_hello("SP")
#person1 = Greeting("sptan1", "KL")
# person1.say_hello("shupei")


# mystring = "hello world"
# mystring.capitalize()

# mystring = str("hello world")
# result = mystring.capitalize()
# print(result)


#Person = class
#person = object
#surname = function parameter
#self = reference to instance of a class
#age = function = method
#age = local variable
#self.email = instance variable
#person.email = object variable

# import datetime # we will use this for date objects
# class Person:
#     def __init__(self, name, surname, birthdate, address, telephone, email):
#         self.name = name
#         self.surname = surname
#         self.birthdate = birthdate
#         self.address = address
#         self.telephone = telephone
#         self.email = email
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, 
#         self.birthdate.day):
#             age -= 1
#         return age

# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )

# print(person.name)
# print(person.email)
# print(person.age())


# person1 = Person(
#     "SP",
#     "Tan",
#     datetime.date(1983, 7, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "sptan1example.com"
# )

# print(person1.name)
# print(person1.email)
# print(person1.age())








# class MyString(str) :
#     def __init__(self,astring):
#         self.astring = astring

#     def reverse(self):
#         reversedstring = ""

#         for char in self.astring:
#             reversedstring = char + reversedstring

#         return reversedstring

# name = MyString("alim")
# print(name.reverse())

# print(name.capitalize())

# class Car:
#     def __init__(self, color, name, model) :
#         self.color = color
#         self.name = name
#         self.model = model

#     def baseInfo(self):
#         print("base model")

# class ElectricCar (Car):
#     def detail(self):
#         print(f'Electric car {self.color} {self.name} {self.model}')

# #car1 = Car("Green", "Honda","Civic")
# ec = ElectricCar("Green", "Honda","Civic")
# #print(car1.name)
# ec.detail()
# ec.baseInfo()


# class Parent(object):

#     def __init__(self,parentVar):
#         self.parentVar = parentVar

#     def implicit(self):
#             print("Parent implicit()")

#     def override(self):
#         print("Parent override()")

#     def altered(self):
#         print("Parent altered()")

# class Child(Parent):
#     def __init__(self,stuff,parentVar):
#         self.stuff = stuff
#         super(Child, self).__init__(parentVar)

#     def override(self):
#         print("Child override()")
#     #pass

#     def altered(self) :
#         print("Child, before Parent altered()")
#         super(Child,self).altered()
#         super(Child,self).altered()
#         print("Child, after parent altered()")

# #dad = Parent()
# #dad.implicit()
# #dad.override()

# son = Child("Chair",200)
# print(son.stuff)
# print(son.parentVar)
# #son.altered()
# #son.override()
# #son.implicit()

# class Vehicle :
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print(f'car.print_info() {self.year} {self.make} {self.model}')

# car = Vehicle("Nissan", "Leaf", 2015)

# print(car.make, car.model, car.year)
# car.print_info()


# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
    
#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact_info(self):
#         print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

#     def friends(self,friend):
#         (self.friends).append(friend)
#         print(self.friends)

# person1 = Person(
#     "Sonny",
#     "sonny@hotmail.com",
#     "483-485-4948"
# )

# person2 = Person(
#     "Jordan",
#     "jordan@aol.com",
#     "495-586-3456"
# )

# person1.greet(person2)
# person2.greet(person1)

# #print(person1.email,person1.phone)
# #print(person2.email, person2.phone)

# person1.print_contact_info()
# person2.print_contact_info()

# person2.friends("Sonny")



class Student:
    def __init__(self, firstName, lastName, campus):
        self.firstName = firstName
        self.lastName = lastName
        self.campus = campus

    def printStudent(self):
        print(f'{self.firstName}, {self.lastName}, {self.campus}')

#eric = Student("Eric", "Deveder","Houston")

class Campus:
    def __init__(self):
        self.students = []

    def addStudent(self,firstName,lastName,campus):
        temp = Student(firstName, lastName, campus)
        self.students.append(temp)

    def showCurrentStudent(self):
        for studentObj in self.students:
            print(f'{studentObj.firstName} {studentObj.lastName}')

    def showIndex (self, index):
        print(f'{self.students[index].firstName}')


dc = Campus()
dc.addStudent("Eric", "Develder", "Houston")
dc.addStudent("Gustavo", "Fette", "BA")
dc.addStudent("Thomas", "Morrow", "Houston")

dc.showIndex(1)
