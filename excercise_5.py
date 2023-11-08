import functools

numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers = functools.reduce(lambda counter, item: counter + item, numbers)
print(numbers)
