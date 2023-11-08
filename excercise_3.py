items = [
    {"product": "Shirt", "price": 100}, {"product": "Pants", "price": 300}, {"product": "Shoes", "price": 200}
]


def applyTaxes(percentage):
    return [
        {"product": item["product"],
         "price": item["price"],
         "taxes": item["price"] * percentage / 100}
        for item in items
    ]


def applyIva(percentage, arr):
    return list(map(lambda item: {"product": item["product"],
                                  "price": item["price"],
                                  "iva": item["price"] * percentage / 100}, arr))


itemsWithTaxes = applyTaxes(19)
itemsIva = applyIva(19, items)

print(items)
print(itemsWithTaxes)
print(itemsIva)
