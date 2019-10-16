def add_one(num):   # num is a parameter (and a variable), the scope of a parameter is the function body
    num = num + 1   # start of the function body
    return num      # start of the function body

def something(a, b):
    a = a + 2
    b = b - 2
    return a, b


print(something(2, 3))


myint = 8           # define a variable and initialise it
print(myint)        # supply a variable as an argument

myint = add_one(myint)  # myint is an argument

print(myint+1)     # use an arithmetic expression as an arguement

num = 666

print(add_one(num))  # use a function call as an argument, OR ue the return value of a function call as an arguement

print( add_one(999) )  # use a constant as an argument,

str = 'this is a string'+' innit'
print(str)

mytuple = something(myint, num)

print(mytuple[1], mytuple[0])



print(type(something(2, 3)))

print(3 == 4)





