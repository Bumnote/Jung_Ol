def solution(month, day):
    if 1 <= month <= 12:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (1 <= day <= 31):
            print("OK!")
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (1 <= day <= 30):
            print("OK!")
        elif month == 2 and (1 <= day <= 29):
            print("OK!")
        else:
            print("BAD!")
    else:
        print("BAD!")


month, day = map(int, input().split())
solution(month, day)
