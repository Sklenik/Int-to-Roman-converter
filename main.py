#function that converts int() to roman numerals

import sys

try:
    number = sys.argv[1]
except IndexError:
    print('ERROR - incorrect number of arguments')
    exit()

def roman(number):
    if not isinstance(number,int):
        try:
            number = int(number)
            roman(number)
        except NameError:
            print('ERROR - invalid input')
        except ValueError:
            print('ERROR - invalid input')

#ths - thousand, hun - hundred, ten - tens, ons - ones
          
    elif number >0 and number <= 3999:
        ths = number//1000
        rem1 = number%1000
        hun = rem1//100
        rem2 = rem1%100
        ten = rem2//10
        ons = rem2%10

        M = ths*'M'
        CM = (hun//9)*'CM' + ((hun%9)//5)*'D' + (((hun%9)%5)//4)*'CD' + (((hun%9)%5)%4)*'C'
        XC = (ten//9)*'XC' + ((ten%9)//5)*'L' + (((ten%9)%5)//4)*'XL' + (((ten%9)%5)%4)*'X'
        IX = (ons//9)*'IX' + ((ons%9)//5)*'V' + (((ons%9)%5)//4)*'IV' + (((ons%9)%5)%4)*'I'
        
        print(M+CM+XC+IX)
    
    else:
        print('ERROR - input must be a positive integer smaller than 3999')

roman(number)
