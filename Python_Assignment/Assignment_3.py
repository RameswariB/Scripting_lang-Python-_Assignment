def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

def DecimalToOctal(num):
    if num >= 1:
        DecimalToBinary(num // 8)
    print(num % 8, end = '')


dec_val = int(input('Enter number :'))
print("Binary NUmber is :")
DecimalToBinary(dec_val)
print('\n Octal Number is :')
DecimalToOctal(dec_val)