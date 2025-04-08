import time
import sys 
from time import gmtime

def user_choice(choice):

    if choice =='1':
        digital_clock()
    elif choice == '2':
        seconds = int(input('Enter the number of seconds:'))
        countdown_timer(seconds)
    else:
        print('Invalid Choice')


def digital_clock():
    while True:
        current_time = time.gmtime()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",current_time)
        
        print(f"\rCurrent time:{formatted_time}",end='',flush=True)
        
        time.sleep(5)

    
def countdown_timer(seconds):
    
    while seconds:
        
        timer = '{:02d}'.format(seconds)
        print(f'\r{timer}', end='', flush=True)
        time.sleep(1)
        seconds -= 1

    print('\nTime is up!')


if __name__ == '__main__':
    while True:
        user_input = input('Enter the number(1:Digital Clock),(2:Countdown Timer)')
        user_choice(user_input)




