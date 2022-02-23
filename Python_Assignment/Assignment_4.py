def get_factor(number):
    value=1;
    sum=0;
    while(value < number):
        if(number%value == 0):
            sum+=value;
        value=value+1
    return sum

def check_relation(num1,num2):
    sum1=get_factor(num1)
    print(f'{num1} factor is {sum1}')
    sum2=get_factor(num2)
    print(f'{num2} factor is {sum2}')
    if(num1 == sum2 or num2 == sum1):
        print(f"{num1} and {num2}  has relation")
    else:
        print(f"{num1} and {num2}  has no relation")


number = int(input("Please Enter any Number1: "))
number2 = int(input("Please Enter any Number2: "))
check_relation(number,number2)







