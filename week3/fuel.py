# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is
# 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is
# essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure
# to catch any exceptions like ValueError or ZeroDivisionError.

while True:
    try:
        fuel_tank = (input("Fraction: "))
        fraction = fuel_tank.split('/')

        numerator = int(fraction[0])
        denominator = int(fraction[1])
        percentage = round((numerator/denominator)*100)


        ## DEBUGGING ##

        # print("percentage: ",percentage)
        # print("denominator: ",denominator)
        # print("numerator: ", numerator)

        # print("type percentage: ",type(percentage))
        # print("type denominator: ",type(denominator))
        # print("type numerator: ", type(numerator))

        if numerator > denominator:
            continue

        if percentage >= 99:
            print("F")
            break

        if percentage <= 1:
            print("E")
            break

        else:
            print(f"{percentage}%")
            break

    except ValueError:
        pass

    except ZeroDivisionError:
        pass
