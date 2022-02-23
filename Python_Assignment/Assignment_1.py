import statistics

choice = False
number: int = [1, 2, 3, 4, 5, 6, 7, 8]


while(choice == False):
    print('P - Print numbers')
    print('A - Add a number')
    print('M - Display mean of the numbers')
    print('S - Display the smallest number')
    print('L - Display the largest number')
    print('Q - Quite')
    inputData = input('Enter your choice :')

    if (inputData.upper() == 'P'):
        print(number)
    elif (inputData.upper() == 'A'):
        addNumber: int = int(input('Enter NUmber you want to add:'))
        number.append(addNumber)
        print(number)
    elif (inputData.upper() == 'M'):
        print('mean : ', statistics.mean(number))
    elif (inputData.upper() == 'S'):
        smallNum=min(number);
        print('smallest Number :',smallNum)
    elif (inputData.upper() == 'L'):
        largestNum=max(number)
        print('largest Number :',largestNum)
    elif (inputData.upper() == 'Q'):
        choice = True;
        break;
    else:
        print('Error');
