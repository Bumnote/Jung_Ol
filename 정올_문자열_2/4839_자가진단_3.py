arr = list(input())

for i in range(len(arr)):
    for first in range(len(arr) - i - 1, len(arr)):
        print(arr[first], end="")

    for second in range(len(arr) - i - 1):
        print(arr[second], end="")
    print()
