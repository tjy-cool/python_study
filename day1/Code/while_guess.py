#/usr/bin/env python
# Author:tjy

_age = 25


count = 0
while count < 3 :    # True
#    if count == 3 :
#       break
    guess_age = int(input("age:"))
    if _age == guess_age :
        print("you got it")
        break
    elif _age > guess_age :
        print("guess bigger　!!!")
    else :
        print("guess smaller !!!")
    count += 1
else :
#if count == 3 :
    print("you have tried too many times ... fuck off")