countries_a = {"col", "mex", "bol"}
countries_b = {"pe", "bol"}

# Unión
# Toma todos los elementos de los dos conjuntos
print("------ unión ------")
print(countries_a.union(countries_b))
print(countries_a | countries_b)

# Intersección
# Toma los elmentos que son comunes en ambos conjuntos
print("------ Intercepción ------")

print(countries_a.intersection(countries_b))
print(countries_a & countries_b)

# Diferencia
# Resta o quita (anula) los elementos del conjunto que se encuentra en el lado derecho de la operación
print("------ Diferencia ------")

print(countries_a.difference(countries_b))
print(countries_a - countries_b)

# Diferencia simetrica
# Toma los elementos que no son comunes entre los dos conjuntos
print("------ dif simetrica ------")
print(countries_a.symmetric_difference(countries_b))
print(countries_a ^ countries_b)
