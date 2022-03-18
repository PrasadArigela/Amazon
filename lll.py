a = -10
b = 10.5
c = 10j

print(type(a))
print(type(b))
print(type(c))

# Keyword Shows The List 
import  keyword
print(keyword.kwlist)

# The Reverse string Of prasad
str = "prasad"
str1 = " "
for i in str:
   str1 = i + str1
print("The Reverse String is:",str1)

# Array of string
a = "string"
print(a[0:4])

# Swap Two Number 
x = 10
y = 20

x,y = y,x
print("After Swaping Of x is:",x)
print("After Swaping of y is:",y)


a = "priy@nk@ prasad"
b=a.split(" , ")
print(b)

txt = "my name is prasad, and i am {}"
age = 24

print(txt.format(age))


txt = "this is {}, and  comming in {}, and my age is{}"
str = "prasad"
str1= "Hyderabad"
age = 24
print(txt.format(str,str1,age))

age = "twenty \bfour"
print(age)


age = "This is prasad and my is \"24\" ,and i am \"youngest son \" in my family"
print(age)

age = "It\'s  \nvery Important"
print(age)

txt = "\"Prasad\",\nPriya"
print(txt)

age = "prasad AND THIS IS VERY IMPORTANT"
print(age.partition("THIS"))

name = "HELLO_WELCOME"
print(name.capitalize())

x = ("name","raju","time","puja","roja","uptime")
y = list(x)
y.append("orange")
x = tuple(y)

text = "HELLO WELCOME to apple and apple color is red, the apple is very tasty"
print(text.count("apple"))

name = "prasad"
print(name.center(100))

name = "   ram prasad  "
x = name.lstrip()
print("my name is:", x, " and iam handsome")

list = ["Student_Name","Age","Height","Roll_Number"]
tuple = ("ram_prasad","24",154.5)
list.extend(tuple)
for i in list:
     print(i)
     
list = ["ram","love","redme","chat"]
[print(x) for x in list if x != "ram"]



