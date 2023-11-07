import random

exponents = {i: i ** 2 for i in range(1, 11)}
print(exponents)

countries = ["col", "mex", "bol", "pe"]

population = {country: random.randint(1, 100) for country in countries}
print(population)

population = {country: population for (country, population) in population.items() if population > 50}
print(population)

text = "Hola, soy Ernesto"
vowels = {c: c.upper() for c in text if c in "aeiou"}
print(vowels)
