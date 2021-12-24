def solution(arr, n, cnt):
    if n == cnt:
        print(arr[- 1])
        return

    arr.append((arr[-2] * arr[-1]) % 100)
    return solution(arr, n, cnt + 1)


arr = [1, 2]
n = int(input())
cnt = 2
solution(arr, n, cnt)
