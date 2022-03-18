a = "names of Collage"
c = a.capitalize()
d = a.swapcase()
e = a.title()
print(c)
print(d)
print(e)

b = "na\tm\te"
x = b.expandtabs()
print(x)

b = "hello wold"
f = {45: 49}
v = b.translate(f)
print(v)

car = {"brand" : "volvo","model" : "somen", "year" : 2014,"color" : "red"}
x = car.items()
print(x)
car["ciaz"] = "white"
print(x)



myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
print(myfamily)

for i in range(0,10):
    print(i)
    if i == 5:
       break
    else:
       print("Finall reached is the statement")
    
    
def name(fname):
    print("the first name is:",fname)
    
name("prasad")


def trirecursion(k):
   if(k>0):
      result = k + trirecursion(k-1)
      print(result)
   else:
     result = 0
   return  result
print("\n\nRecursion Example Results")
trirecursion(5)


def fac(n):
    return 1 if(n==1 or n==0) else n * fac(n-1)
n = 5
print("the",n,"factorial of is:",fac(n))

def func(n):
  return lambda a : a + n
myfunc = func(5)
print("After existing lambda function  additon value is:",myfunc(5))

def trirecursion(n):
   if (n > 0):
     result = n + trirecursion(n-1)
     print(result)
   else:
     result = 0
   return result
trirecursion(6)


str = "name"
str1 = " "
for i in str:
    str1 = i + str1
print("The string is reverse:",str1)
for j in str1:
    print("The is line by line:",j)
    
    
    
a = "   ram  "
x = a.lstrip()
print("The Name is",x)