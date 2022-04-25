print("Enter The String: ", end="")
text = input()
textlenght = len(text)
for char in text:
   ascii = ord(char)
   print(char," ",ascii)
