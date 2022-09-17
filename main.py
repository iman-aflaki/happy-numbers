import math


def is_happy(num):
    included = set()
    while num != 1:
        num = sum(int(i)**2 for i in str(num))
        if num in included:
            return False
        included.add(num)
    return True


counter = 0
number = 1
list1 = []
while counter <= 20:
    if is_happy(number):
        list1.append(number)
        counter += 1
        number += 1
    else:
        number += 1
print(list1)
