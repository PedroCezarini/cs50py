#não passou no teste: preferredFirstName

word = input ("camelCase: ")
aux1 = word
words = []

for letter in word:
    if letter.isupper():
        aux = letter.casefold()
        words = word.split(letter)
        #camel_case = words[0] + "_" + aux + words[1]
        print("snake_case: " + words[0] + "_" + aux + words[1])

    elif aux1.islower():
        print("snake_case: " + aux1)
        break