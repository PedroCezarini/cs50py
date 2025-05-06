# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U)
# omitted, whether inputted in uppercase or lowercase.

#1. input usuario
phrase = input("Input: ")

#2. usando maketrans pra fazer uma tabela de mapeamento de caracteres
vowels = str.maketrans(' ',' ', "aeiouAEIOU")

#3. chamando translate para fazer as substituiçoes na phrase (remover as vogais)
new_phrase = phrase.translate(vowels)

print(new_phrase)
