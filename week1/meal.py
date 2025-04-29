#breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

#In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
#If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
#And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

#Structure your program per the below:
#wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
#For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    x = input("What time is it? ").split(':')
    y = convert(x)

    if y >= 7 and y <= 8:
        print("breakfast time")

    elif y >= 12 and y <= 13:
        print("lunch time")

    elif y >= 18 and y <= 19:
        print("dinner time")

#tentar fazer retorno em vez de print


def convert(time):
    horaFloat=float(time[0])
    minFloat=float(time[1]) / 60
    horaRefeicao = horaFloat + minFloat
    return horaRefeicao

if __name__ == "__main__":
    main()
