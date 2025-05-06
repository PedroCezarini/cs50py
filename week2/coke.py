amount_due = 50

print("Amount Due:", amount_due)

while amount_due > 0:
    inserted_coin = input("Insert coin: ")

    if inserted_coin.isdigit():
        inserted_coin = int(inserted_coin)

        if inserted_coin in [5, 10, 25, 50]:
            amount_due -= inserted_coin
        else:
            print("Coin not accepted.")
    else:
        print("Please insert a valid number.")

    if amount_due > 0:
        print("Amount Due:", amount_due)
    
    else:
        print("Change Owed:", abs(amount_due))
