grocery_list = []
grocery_dict = {}

while True:
    try:
        item = input().upper() #input do item
        grocery_list.append(item) #adiciona item a grocery_list
        x = grocery_list.count(item) #conta quantas vezes o item inserido aparece em grocery_list
        grocery_dict.update({item: x}) #atualiza o dicionario com o item e quantas vezes apareceu

    except ValueError:
        pass

    except EOFError:
        sorted_grocery_dict = dict(sorted(grocery_dict.items())) #linha pra ordenar o dicionario por ordem alfabetica
        for item, x in sorted_grocery_dict.items(): #pra cada chave e valor no dicionario
            print(x, item) #imprime valor e chave conforme pedido no exercicio
        exit()

    else:
        pass
