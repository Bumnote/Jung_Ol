def solution(arr):  # bubble Sort
    for y in range(len(arr) - 1):
        for x in range(len(arr) - 1):
            if arr[x] < arr[x + 1]:
                temp = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = temp
        for t in arr:
            print(t, end=" ")
        print()


arr = list(map(int, input().split()))
solution(arr)
