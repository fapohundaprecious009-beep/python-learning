# Working with Strings
#concatenation(to join)
name="Hello" + " " + "Precious"
print(name)

name="Precious"
print("Hello {}".format(name))

firstName="Precious"
lastName="Fapohunda"
print("Hello {} {}".format(lastName, firstName))
print(f"Hello {firstName}")

#using Camel case (firstName)
print(firstName[5])
print(lastName[-1])

# slicing
Name="FapohundaPrecious"
print(Name[0:9])
print(Name[9:17])
print(Name[0:17:2])
# order: start, stop, Step

#title
Name="fapohunda precious"
print(Name.title())

Name="FAPOHUNDA PRECIOUS"
print(Name.lower())
# upper to make it capital letter

print(Name.find("precious"))

Name="      My name is Fapohunda Precious!     "
print(Name.strip())
#The strip function removes the space at the beginning and end of a string

Name="My name is Fapohunda Precious!"
print(Name.split(" "))
#split breaks the word 

#User Input
print(input("What is your name? "))

name=(input("What is your name? "))
print("Hello, My name is", name )

