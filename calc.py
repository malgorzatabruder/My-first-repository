a=1
b=1
def addition(a,b):
    value=a+b
    return value
def subtraction(a,b):
    value=a-b
    return value
def multiplication(a,b):
    value=a*b
    return value
def division(a,b):
    if b!=0:
        value=a/b
        return value
    else:
        print('Dividing by 0 is incorrect, choose another number')
def power(a,b):
    value=pow(a,b)
    return value
operators=['+','-','*','/','^']
#main menu

while True:
    a=input('Welcome to my calculator! Please choose first number:\n')
    b=input('Choose the second number:\n')
    operator=str(input('Please choose the operator you want to use:\n'))
    if not a or not b or not operator:
        break
    else:
        try:
            a=int(a)
            b=int(b)
            if not operator in operators:
                print('Operator does not exist')
                continue
        except:
            print("You should input number")
            continue
        if operator=='+':
            print("Your result is: "+str(addition(a,b)))
        elif operator=='-':
            print("Your result is: "+str(subtraction(a,b)))
        elif operator=='*':
            print("Your result is: "+str(multiplication(a,b)))
        elif operator=='/':
            print("Your result is: "+str(division(a,b)))
        elif operator=='^':
            print("Your result is: "+str(power(a,b)))
        else:
            print('Operator is incorrect. Try again.')

   
    
