#Program to create a list
list1 = ['a', 'b', 'c', 'd']
shows = [ 'The Big Bang Theory', 'Friends','the office', 'Seinfield',]
flowers = ['daisy', 'peony', 'rose', 'lily', 'daffodil']
cars = ['Suzuki', 'Honda', 'BMW', 'Porsche', 'Volkswagon']
print(shows)
print(flowers)
#Using sort function to sort the elements of list
shows.sort()
print(shows)

#Determining the length of a list
flowers_length = len(flowers)
print(flowers_length)

#Accessing an element from the list
a = cars[4]
print(a)

#Adding an element in a list
shows.append("The Crown")
print(shows)

shows[0] = "Suits"
print(shows)

flowers.insert(2,'lavender')
print(flowers)

#Removing an element from a list
shows.remove("The Crown")
print(shows)

cars.pop(2)
print(cars)

#Accessing the elements in a list by indexing

""" For directly accessing the last element"""
print(flowers[-1])

""" For selecting last n elements"""
print(cars[-3:])

"""To select everything except last n elements"""
print(list1[:-2])

