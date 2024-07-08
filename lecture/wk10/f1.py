import store

# help(store)

print(store.name)
print(store.since)

store.name = "New Store Name"

print(store.name)

print("this value", "and that value", sep="--", end=".!.!\n")

price = store.order_in_store("food", 5)

print(price)

price1 = store.order_in_store("drink", 3)
print(price1)

store.order_in_store(quantity=50, product="clothes") # named arguments


saved_doc1 = store.__doc__
print(saved_doc1)