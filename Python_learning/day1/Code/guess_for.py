#/usr/bin/env python
# Author:tjy

# for i in range(10) :
#     print("loop ", i)
# for i in range(1,10,2):
#     print(i)

_age = 25
for i in range(3) :
    guess_age = int(input("age:"))
    if _age == guess_age :
        print("you got it")
        break
    elif _age > guess_age :
        print("guess bigger　!!!")
    else :
        print("guess smaller !!!")
else :
    print("you have tried too many times ... fuck off")
