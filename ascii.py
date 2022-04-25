print("Enter The String: ", end="")
text = input()
textlenght = len(text)
for char in text:
   ascii = ord(char)
   print(char," ",ascii)
   
 
i = 10
if i % 2 == 0:
   print("The Number is Even Number:")
else:
   print("The Number is Odd Number:")
   
