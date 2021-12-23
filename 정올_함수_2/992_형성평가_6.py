def solution(arr):
    for i in range(3):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    for i in arr:
        print(i, end=" ")


arr = list(map(int, input().split()))
solution(arr)
