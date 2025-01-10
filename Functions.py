#without input and without return statement
def add():
    a=20
    b=10
    print('addition is:',a+b)
add()

#with input and without return statement
def sub(a,b):
    print('Subtraction is:',a-b)

 #without input and with return statement 
 def mul(a,b):
    return 10*3

#with input and with return statement
def div(a,b):
    return a/b

add()
sub(22,12)
print(mul())
print(div(12,6))

