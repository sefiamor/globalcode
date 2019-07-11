#simple calculator
def calculate():
   print('choose any of the functions you want to work with')
   print('A. Addition')
   print('B. Subtraction')
   print('C. Multiplication')
   print('D. Division')
   z=input('enter the selected value: ')
   if z=="A"or'a':
    x=input('enter your first number: ')
    y=input('enter your second number: ')
    s=x
    t=y
    result=int(s)+int(t)
    print('your answer is: ',result)
   elif z=='B'or'b':
    x=input('enter your first number: ')
    y=input('enter your second number: ')
    s=x
    t=y
    result=int(s)-int(t)
    print('your answer is: ',result)
   elif z=='C'or'c':
    x=input('enter your first number: ')
    y=input('enter your second number: ')
    s=x
    t=y
    result=int(s)*int(t)
    print('your answer is: ',result)
   elif z=='D'or'd':
    x=input('enter your first number: ')
    y=input('enter your second number: ')
    s=x
    t=y
    result=s/t
    print('your answer is: ',result)
   else:
    print('Your have entered a wrong value..., please RETYPE')
    z=input('enter the selected value: ')
 

calculate()
