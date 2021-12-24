def solution(n, arr, index):
    if index > n:
        print(arr[-1])
        return

    arr.append(arr[index // 2] + arr[index - 1])
    return solution(n, arr, index + 1)


n = int(input())
arr = [0, 1]
index = 2
solution(n, arr, index)
