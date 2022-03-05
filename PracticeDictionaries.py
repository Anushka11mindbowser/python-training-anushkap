demo_dict = {'rose': 'red', 'lily':  'white', 'sunflower': 'yellow', 'hibiscus': 'red' }

#Accesing different part of dictionaries

print(demo_dict.keys())
print(demo_dict.values())
print(demo_dict.items())
print(demo_dict.get('rose'))
print(demo_dict.get('daffodil', 'daffodil does not exist'))

#Adding and Deleting items from a dictionary

print(demo_dict.pop('sunflower'))
demo_dict['sunflower'] = 'yellow'
print(demo_dict)

demo_dict.popitem()
print(demo_dict)

demo_dict['rose' ] = 'pink'
print(demo_dict)

