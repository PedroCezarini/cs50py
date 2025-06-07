#1. precisa colocar o try except pra continuar pedindo input se usuario colocar entrada errada
#2. precisa fazer a verificação dos dias (<32)
#3. precisa fazer a verificação dos meses no caso de int: <13
#4. precisa fazer a verificação dos meses no caso de string: tem que estar na month_list

month_list = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    user_date = input("Date: ")
    user_date = user_date.strip()
    user_date_int_test = user_date.replace("/","0") #teste vei podi pra ver qual o formato da entrada do usuario

    class InvalidDayNumber(Exception):
        pass

    class InvalidMonth(Exception):
        pass

    if user_date_int_test.isdigit() == True:
        try:
            date_info = user_date.split("/")
            month = int(date_info[0])
            day = int(date_info[1])
            year = int(date_info[2])

            if day > 31:
                raise InvalidDayNumber

            elif month > 12:
                raise InvalidMonth

            else:
                print(f"{year}-{month:02}-{day:02}", end="")
                exit()

        except ValueError:
            pass

        except InvalidDayNumber:
            pass

        except InvalidMonth:
            pass

    else:
        try:
            date_info = user_date.split(" ")
            day = int(date_info[1].rstrip(","))

            if "," not in date_info[1]:
                raise ValueError

            if day > 31:
                raise InvalidDayNumber

            for month_name, value in month_list.items():

                if month_name == date_info[0]:
                    month = int(value)

                    if month > 12:
                        raise InvalidMonth

                    else:
                        print(f"{date_info[2]}-{month:02}-{day:02}", end="")
                        exit()

                else:
                    pass

        except ValueError:
            pass

        except InvalidDayNumber:
            pass

        except InvalidMonth:
            pass

        except IndexError:
            pass
