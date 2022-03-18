# 1)Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# 2)Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# 3)Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)

# 4)Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# 5)Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)

# 6)Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# 7)Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

# 8)Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# 9)Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# 10)Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


t = set(("ram","raju","ram_prasad","list"))
b = ["name","ghbt","namer"]
t.intersection(b)
print(t)


