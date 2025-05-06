# Solução mais simples e funcional

word = input("camelCase: ")
snake_case = ""

for letter in word:
    if letter.isupper():
        snake_case += "_" + letter.casefold()

    else:
        snake_case += letter

print("snake_case: " + snake_case)
