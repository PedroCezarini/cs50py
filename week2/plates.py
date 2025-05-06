# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isdigit() or s[1].isdigit():
        return False

    if not s.isalnum():
        return False

    found_number = False #startando numero achado como falso

    for i in range(len(s)):

        if s[i].isdigit():      #achou um numero na placa

            if not found_number: #se for o primeiro numero

                if s[i] == '0':   #se esse numero for 0
                    return False#retorna falso pq primeiro numero eh 0

                found_number = True #se for diferente de 0 seta found_number pra verdade

        else:                   #não achou numero na placa
            if found_number:    #se found_number = verdadeiro
                return False    # retorna falso pq


    return True

main()
