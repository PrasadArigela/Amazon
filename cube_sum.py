#Step 1- Define a function to find the cube sum
#Step 2- Declare a variable that will store the sum
#Step 3- Define a loop that will run n times
#Step 4- Inside the loop update the value of the variable which will store the cube sum
#Step 5- Calculate cube of each number before adding it to the sum
#Step 6- Return the value of sum
#Step 7- Take input of n from the user
#Step 8- Pass the input as a parameter in the function
#Step 9- Display the result returned by the function

def cube_sum(n):
   sum = 0
   for i in range(1,n+1):
      sum += i * i * i
    
   return sum
n = 5
print("the sum of cube series is:",cube_sum(n))    