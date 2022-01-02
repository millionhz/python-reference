from item import Item
from phone import Phone

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

items = [item1, item2, item3, item4, item5]

for instances in items:
    print(instances)

#########################

data = [
    ("Phone", 100, 1),
    ("Laptop", 1000, 2),
    ("Cable", 50, 5)
]

items = Item.instantiate_objects(data)

for instances in items:
    print(instances)

######################

phone1 = Phone("Nokia", 100, 14)
phone2 = Phone("Apple", 10000, 3)


print(phone1)
print(phone1.calculate_price())
phone1.apply_discount()
print(phone1.calculate_price())

########################

item = Item("MyItem", 750, 1)
print(item.name)

item.name = "NewName"

print(item)

item.apply_increment(.2)
print(item.calculate_price())
