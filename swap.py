x = int(input("Enter first number "))
y = int(input("Enter second number "))
x = x ^ y
y = x ^ y
x = x ^ y
print("After swapping")
print('x is '+str(x))
print('y is '+str(y))
