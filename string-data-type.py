myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print(" ")

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print(" ")

name = input("What is your name? ")
print("Halo "+name)
print(" ")

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
print(str(name) + ", you like a " + str(color) + " " + str(animal) + " !")
print(" ")