#Creating demo set

demo_set = {15, 18, 14, 23, 50, 15}
print(demo_set)
mixed_set = {'Matilda', 18, 165.5, True}
books = {'The Great Gatsby', 'The Kite Runner', 'Ikigai', 'Little Women', '1984'}
house_items = {'curtains', 'planters', 'lamps', 'wallpiece', 'crockery', 'Coffee Table'}
house_furniture = {'Coffee Table', 'Bean Bag', 'TV Unit', 'Shelves'}

 #Adding elements

books.add("War and Peace")
print(books)
books.update(["Kafka on the Shore", "Pride and Prejudice"])
print(books)

#Deleting an element

books.remove('1984')
print(books)

books.discard('Rumi')
print(books)

books.pop()
print(books)

#Set Operations

"""Union Operator"""
print(house_items|house_furniture)
print(house_furniture.union(house_items))

"""Intersection"""
print(house_items & house_furniture)
print(mixed_set.intersection(demo_set))

"""Set Difference"""
print(house_furniture - house_items)
print(house_items - house_furniture)

print(house_furniture.difference(house_items))
print(house_items.difference(house_furniture))

"""Symmetric Difference"""

print(house_furniture ^ house_items)
print(house_items ^ house_furniture)

#Check for subset
print(house_furniture.symmetric_difference(house_items))
housie = {'lamps', 'curtains', ' planters'}
a = housie.issuperset(house_items)
print(a)

