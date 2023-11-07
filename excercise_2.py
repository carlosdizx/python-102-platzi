numbers = [1, 2, 3, 4, 5]
print("Original numbers", numbers)

numbers = list(map(lambda i: i ** 2, numbers))
print("Operated numbers ", numbers)

prime_numbers = [2, 3, 5, 7, 11]
print("Prime numbers", prime_numbers)

result = list(map(lambda x, y: x * y, numbers, prime_numbers))
print("Operated numbers * prime numbers (x,y) = x*y", result)
