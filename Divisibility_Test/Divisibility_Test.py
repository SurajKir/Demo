from Divide import divide


def StringIsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def DigitAddition(string):
    if(len(string)<=2):
        return int(string)
    else:
        sum = 0
        for i in string:
            sum += int(i)
        
        return DigitAddition(str(sum))


def DivisibleBy2(string):
    if(StringIsInt(str(divide(int(string[-1]),2)))):
        return True
    else:
        return False


def DivisibleBy3(string):
    StrAdd = DigitAddition(string)
    if(StringIsInt(str(divide(StrAdd,3)))):
        return True
    else:
        return False


def DivisibleBy4(string):
    if(StringIsInt(str(divide(int(string[-2:]),4)))):
        return True
    else:
        return False


def DivisibleBy5(string):
    if(int(string[-1])==5 or int(string[-1])==0):
        return True
    else:
        return False


def DivisibleBy6(string):
    if(DivisibleBy2(string) and DivisibleBy3(string)):
        return True
    else:
        return False


def DivisibleBy7(string):
    if(len(string)<=2):
        if(StringIsInt(str(divide(int(string),7)))):
            return True
        else:
            return False
    else:
        LastDigit = string[-1]
        RemainingString = string[0:(len(string)-1)]
        Result = int(RemainingString) - int(LastDigit)
        return DivisibleBy7(str(Result))
    return False


def DivisibleBy8(string):
    if(StringIsInt(str(divide(int(string[-3:]),8)))):
        return True
    else:
        return False


def DivisibleBy9(string):
    StrAdd = DigitAddition(string)
    if(StringIsInt(str(divide(StrAdd,9)))):
        return True
    else:
        return False
    

number = input('Enter the no. :')
print('The no. is divisible by the following numbers:')
DivisibleBy = [DivisibleBy2(number), DivisibleBy3(number), DivisibleBy4(number), DivisibleBy5(number),
                DivisibleBy6(number), DivisibleBy7(number), DivisibleBy8(number), DivisibleBy9(number)]

for i in range(0,8):
    if(DivisibleBy[i] == True):
        print(i+2)
        

