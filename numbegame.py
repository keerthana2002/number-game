from random import choice
import time
l=[2,4,6,8,10]
for i in l:
    rand = choice(l)
print("Think of any number")
time.sleep(3)
print("Double it")
time.sleep(4)
print("Add" , rand , "to it")
time.sleep(4)
print("Divide it by 2")
time.sleep(4)
print("Now subtract the number with the number you thought at first")
time.sleep(5)
print("Now let me guess the number you thought!")
ans = rand//2
time.sleep(5)
print(ans)
