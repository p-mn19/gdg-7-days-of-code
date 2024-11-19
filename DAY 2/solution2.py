def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
n = int(input("Enter the number of levels for the pyramid: "))
print_pyramid(n)
