while True:
    width = int(input("Width = "))
    height = int(input("Height = "))
    area = float(width) * height / 2

    print("Triangle Area = %.1f" % (area))
    c = input("Continue? ")
    if c == 'Y' or c == 'y':
        continue
    else:
        break
