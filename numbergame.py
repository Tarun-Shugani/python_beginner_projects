#number game  basic level project:1
#using random package

import random

guess_num = random.randint(0,100)
points = 10

def user_input():
    global num2
    num2 = int(input("Enter a number to guess the given number"))
    return num2


def hint_gen():
    hint_num = random.randint(1, 20)
    action_num = random.randint(1,5)
    if action_num == 1:
        hint = guess_num + hint_num
        print('the sum of the number and ',hint_num ,' is',hint)
    elif action_num == 2:
        hint = guess_num - hint_num
        print('the difference of the number and ', hint_num , ' is'
        ,hint)

    elif action_num == 3:
        hint = guess_num / hint_num
        print('the division of the number and ' , hint_num , ' is'
              , hint)

    elif action_num == 4:
        hint = guess_num * hint_num
        print('the multiplication of the number and ' , hint_num , ' is'
              , hint)

    else:
        hint = guess_num % hint_num
        print('the remainder of the number and ' , hint_num , ' is'
              , hint)




while points > 0:
    hint_gen()
    guess_num1 = user_input()
    if guess_num1==guess_num:
        print('congrats you have find the number, it is ',guess_num,'/n you have scored ',points)
        break
    else:
        print('try again')
        points = points-2
else:
    print('better luck next time')




