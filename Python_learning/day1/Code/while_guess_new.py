#/usr/bin/env python
# Author:tjy

_age = 25
count = 0
while count < 3 :    # True
    guess_age = int(input("age:"))
    if _age == guess_age :
        print("you got it")
        break
    elif _age > guess_age :
        print("guess bigger !!!")
    else :
        print("guess smaller !!!")
    count += 1
    if count == 3 :
        continue_confirm = input("do you want continue(y/n),default y :")
        if continue_confirm != 'n' :
            count = 0
'''
        if continue_confirm == 'n' :
            print("you have exiting the guess...")
        elif continue_confirm == '' or continue_confirm == 'y':
            count = 0
        else :
            print("you have input invalid")
'''
