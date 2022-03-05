#Coding Questions from Coding Bat

#Code Problem: date_fashion

def date_fashion(a, b):
    if (a >= 8 or b>=8):
        print(str(2))

    elif (a <= 2 or b <= 2):
        print(str(0))

    else:
        print(str(1))

print(date_fashion(5,10))
print(date_fashion(5,2))
print(date_fashion(5,5))

# Coding Problem 2
#Code question: squirell_play

def squirell_play(temp, is_summer):
    if (temp >= 60 and temp <= 90) and is_summer == False:
        return True

    elif (temp >= 60 and temp <= 100) and is_summer == True:
        return True

    else:
        return False

print(squirell_play(70, False))
print(squirell_play(95, False))
print(squirell_play(95, True))

