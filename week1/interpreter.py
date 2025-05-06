#prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place
#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z

expression = input ("Enter your expression: ").split(" ")
resultado = 0

if expression[1] == "+":
   resultado = float(expression[0]) + float(expression[2])

if expression[1] == "-":
   resultado = float(expression[0]) - float(expression[2])

if expression[1] == "/":
   resultado = float(expression[0]) / float(expression[2])

if expression[1] == "*":
   resultado = float(expression[0]) * float(expression[2])

print(resultado)
