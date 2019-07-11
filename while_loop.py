# creating a loop function
i = 0
while(i < 10):
    i = i +1
    print(i)

# what is happening in the code above is that, when 'i' is less 10, it will add
# one to the  'i' and print out the value, so it will contuinue looping until
# 'i' is equal or greater than '10' before it will stop looping.  


print(' ')
print(' ')
#printing out numbers from 7 to 19
for x in range(7,20):
    print(x) 

print(' ')
print(' ')
#printing out all even numbers between 12 and 20
for x in range(14,20,2):
    print(x)
print(' ')
print(' ')
#writing  a function called evens that will take two numbers and print all the even numbers between
def evens():
    print('please enter the numbers that you want to see the even numbers between them')
    x=int(input('enter first number: '))
    y=int(input('enter second nunber: '))
    for z in range(x,y):
      if z % 2 ==0:
          print(z)

evens()

def reverse_evens():
    print('please enter the numbers that you want to see the REVERSED even numbers betweeen them') 
    x=int(input('enter first number: '))
    y=int(input('enter second nunber: '))
    for z in reversed(range(x,y)):
      if z % 2 ==0:
          print(z)

reverse_evens()
