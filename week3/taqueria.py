menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0

while True:
    try:
        item = input("Item: ")

        for item_name, item_value in menu.items():
            if item.casefold() == item_name.casefold():
                total = total + item_value
                print(f"Total: ${total:.2f}")

    except ValueError:
        pass

    except EOFError:
        exit()

    except KeyError:
        pass

    else:
        pass


        # DEBUGANDO CÓDIGO NO COMEÇO
        # print(f"item é {item}")
        # print(f"total é {total}")



#TESTES COM WHILE TRUE
# while True:
#     try:
#         x = int(input("Whats X: ")) #deixar so a parte que pode raise a expcetion
#     except ValueError:
#         pass
#     else:
#         break #break no else e print fora do loop
