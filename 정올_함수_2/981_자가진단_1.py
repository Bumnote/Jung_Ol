def solution(arr):
    arr.sort(reverse=True)
    for i in arr:
        print(i, end=" ")


n = int(input())
arr = list(map(int, input().split()))
solution(arr)
