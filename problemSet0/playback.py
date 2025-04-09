#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, 
#replacing each space with ... (i.e., three periods).

print("Enter a phrase here: ")
userphrase = input().replace(' ','...') #Using replace() to replace empty spaces with ...

print (userphrase)