#In a file called bank.py, implement a program that prompts the user for a greeting. 

#If the greeting starts with “hello”, output $0.
#If the greeting starts with an “h” (but not “hello”), output $20. 
#Otherwise, output $100.
#Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

txt = input("Greetings! Now enter your greetings: ").lower()

if txt.startswith("hello"):
    y="$0"
    
elif txt.startswith("h"):
    y="$20"

else:
    y="$100"


print(y)


