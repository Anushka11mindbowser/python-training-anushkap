#Practicing basic class syntax

class DemoClass:
    def __init__(self,a):
        self.a = a

example1 = DemoClass(5)
print(example1.a)


#Defining another function
class Bird:

    #Instantiating class objects
    def __init__(self,name, region):
        self.name = name
        self.region = region

    #Defing class methods
    def display(self, color):
        self.color = color
        print(self.name + " is native to " + self.region)
        print(color)

#Creating objects of class Bird
b1 = Bird('sparrow', 'north africa')
b2 = Bird("robin", 'canada')
b3 = Bird('flemingo', 'florida')
b4 = Bird('woodpecker', 'australia')
b5 = Bird('kingfisher', 'england')

print(b1.display('brown'))

#method to display class attributes
print(dir(Bird))

