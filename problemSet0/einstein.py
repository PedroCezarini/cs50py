#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then 
#outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
#e=mc²

print ("Please insert the mass value in kilograms(using integer numbers): ")
#convertendo o input pra int, pois python sempre pega como string
mass = int(input())
energy = mass * (300000000 * 300000000)
print(energy)