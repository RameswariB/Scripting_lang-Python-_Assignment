import statistics

choice = False
number: int = [1, 2, 3, 4, 5, 6, 7, 8]

def displayMenu():
    print('P - Print numbers')
    print('A - Add a number')
    print('M - Display mean of the numbers')
    print('S - Display the smallest number')
    print('L - Display the largest number')
    print('Q - Quite')

def addNumber():
    addNumber: int = int(input('Enter NUmber you want to add:'))
    number.append(addNumber)
    print(number)

def find_mean():
    tot=0;
    count=0
    for num in number:
        tot=+num
        count+=1
    mean=tot/count
    print('mean',mean)

def find_smallest():
    small=1000;
    for num in number:
        if(num < small):
            small=num;
    print('Smallest Number is ',small)

def find_larger():
    large=0;
    for num in number:
        if(large < num):
            large=num;
    print('largest number is',large)

while(choice == False):
    displayMenu();
    inputData = input('Enter your choice :')
    if (inputData.upper() == 'P'):
        print(number)
    elif (inputData.upper() == 'A'):
        addNumber();
    elif (inputData.upper() == 'M'):
        find_mean();
    elif (inputData.upper() == 'S'):
        find_smallest();
    elif (inputData.upper() == 'L'):
        find_larger();
    elif (inputData.upper() == 'Q'):
        choice = True;
        break;
    else:
        print('Error');
