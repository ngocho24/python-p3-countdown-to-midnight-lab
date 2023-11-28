# your code goes here!
import countdown, countdown_with_sleep
import time

def countdown(number=10):
    while number>0:
        print(f'=>{number} SECOND(S)!')
        number-=1
        print("=>Happy New Year!")


def countdown_with_sleep (number=10):
    while number > 0:
        print(f'=> {number} SECOND(S)!')
        time.sleep(1)  
        number -= 1
    print('=> Happy New Year!')