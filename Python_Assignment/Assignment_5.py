import random

is_correct=False

while(is_correct == False):
    value1 = random.randint(1,10)
    value2 = random.randint(1,10)
    result=int(input(f'how much is {value1} times {value2} ?'))

    if (result == (value1*value2)):
        print('Very good')
        break
    else:
        print('No,Try Again')

