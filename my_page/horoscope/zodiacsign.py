import datetime

def identify_zodiac_sign(day, month, year):
    date_zodiac = {
        "aries": ((3, 21), (4, 20)),
        "taurus": ((4, 21), (5, 20)),
        "gemini": ((5, 21), (6, 21)),
        "cancer": ((6, 22), (7, 22)),
        "leo": ((7, 23), (8, 23)),
        "virgo": ((8, 24), (9, 23)),
        "libra": ((9, 24), (10, 23)),
        "scorpio": ((10, 24), (11, 22)),
        "sagittarius": ((11, 23), (12, 21)),
        "capricorn": ((12, 22), (1, 20)),
        "aquarius": ((1, 21), (2, 20)),
        "pisces": ((2, 21), (3, 20))
    }

    try:
        if year == 0:
            year = datetime.datetime.now().year

        user_date = datetime.date(year, month, day)

        for zodiac, date in date_zodiac.items():
            date_from = datetime.date(year, date[0][0], date[0][1])
            date_to = datetime.date(year, date[1][0], date[1][1])

            if date_from <= user_date and user_date <= date_to:
                return zodiac
        return "capricorn"
    except:
        return "Некорректная дата"




if __name__ == "__main__":
    while True:
        input_date = input('Введите через пробел - день месяц год: ')

        date_split = input_date.split()
        input_day = int(date_split[0])
        input_month = int(date_split[1])
        input_year = int(date_split[2])

        print("Знак зодиака:", identify_zodiac_sign(input_day, input_month, input_year))