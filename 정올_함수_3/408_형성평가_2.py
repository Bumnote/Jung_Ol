def solution_odd(n):
    if n < 0:
        return
    solution_odd(n - 2)
    print(n, end=" ")


def solution_even(n):
    if n == 0:
        return
    solution_even(n - 2)
    print(n, end=" ")


n = int(input())
if (n % 2 == 1):
    solution_odd(n)
else:
    solution_even(n)
