#Code to print a sequence of nos
def print_num(a, b):
    for i in range(a, b+1):
        print(i)
        i= i +1

print(print_num(1,10))

#Code to print cubes of n numbers in sequence

def cube_num(n):
    for i in range(1, n+1):
        print(i ** 3)
        i = i+1

print(cube_num(21))

