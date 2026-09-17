def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


num = 4
result = sum_numbers(num)

print(result)