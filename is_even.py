#a function that accept a value and print out'True' if it's an even number
def even():
  num=int(input('Enter the  number'))
  for i in range(num):
    if i % 2 ==0:
     print(i, 'True')
    else:
     print(i, 'False')

even()
print(' ')
print(' ')
#a function that such or print out the even numbers in the list below

def is_even():
  numbers = [1,56,234,87,4,76,24,69,90,135]
  for i in numbers:
    if i % 2 ==0:
     print(i,"True it's even")

is_even()
print(' ')
print(' ')
#using lambda to write a code that can print out an even number
numbers= [1,56,234,87,4,76,24,69,90,135]
print(filter(lambda x:x % 2 ==0,numbers))

print(' ')
print(' ')

#writing a code that will print out all the odd numbers in the list
def odd():
  numbers = [1,56,234,87,4,76,24,69,90,135]
  for i in numbers:
    if i % 2 !=0:
     print(i,"True it's odd")

odd()


