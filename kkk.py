"""The Maximum Number A and B"""
def maximum(a,b):
   if a >= b:
       return a
   else:
       return b
print("The Maximun Number is:",maximum(4,5))


# Factorial OF Number 
def factorial(n):
  return 1 if (n==1 or n==0) else n * factorial(n-1);
num = 5;
print("Factorial of",num,"is",factorial(num))


#Simple Interest
def Simple_Interset(p,t,r):
   print("The Principle is",p)
   print("The Time Period is",t)
   print("The Rate Of Interest is",r)
   
   si = p * t * r / 100
   print("The Simple Interset is:",si)
   return si
Simple_Interset(8,6,8)


"""The Compound Interest Program"""
def Compound_Interset(principle,rate,time):
    amount = principle*(pow((1+rate/100),time))
    ci = amount - principle
    print("The Compound Interset is",ci)
Compound_Interset(10000,10.5,5)



# Area Of Circle
def find_area(r):
     pi = 3.142
     return pi*(r*r)

print("The Area of Circle is:",find_area(5))


# Print All Prime Numbers
start = 11
end = 25
for i in range(start,end+1):
     if i > 1:
       for j in range(2,i):
         if (i%j==0):
           break
       else:
          print(i)

# check whether a number is Prime or not
num = int(input("Enter The Value is:"))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):

		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number")


# Function for nth Fibonacci number

def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
print("The Fibonacci Number is:",Fibonacci(10))


# Simple Python program to find sum of series
# with cubes of first n natural numbers
# Returns the sum of series
def sumOfSeries(n):
	sum = 0
	for i in range(1, n+1):
		sum +=i*i*i
		
	return sum
n = 20
print("The Sum Of Cube Series Is:",sumOfSeries(n))


# Return the sum of
# square of first n
# natural numbers
def squaresum(n) :

	# Iterate i from 1
	# and n finding
	# square of i and
	# add to sum.
	sum = 0
	for i in range(1, n+1) :
		sum = sum + (i * i)
	
	return sum

# Driven Program
n = 4
print("The Sum Of The Squares Is:",squaresum(n))




