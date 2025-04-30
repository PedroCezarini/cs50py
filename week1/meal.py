def main():
    time = input("Time: ")
    x = convert(time)

    if x >= 7 and x <= 8:
        print("breakfast time")

    if x >= 12 and x <=13:
         print("lunch time")

    if x >= 18 and x <=19:
         print ("dinner time")


def convert(time):
    #time = input("Time: ")
    y = time.split(":")
    hora = float(y[0])
    min = float(y[1]) / 60

    time = hora + min
    float(time)

    #print(time)
    #print(type(time))

    return time

if __name__ == "__main__":
        main()
