def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first, second, end=" ")

    n = n-1
    while n > 0:
        third = first + second

        print(third, end=" ")

        first = second
        second = third
        n -= 1


n = 10
for i in range(n):
    print(recursive_fibonacci(i), end=" ")

print()
non_recursive_fibonacci(n)
