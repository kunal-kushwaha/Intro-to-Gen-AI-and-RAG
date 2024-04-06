import math
def square_and_multiply(num):
    return math.sqrt(num) * 5

user_val = float(input("Enter a positive numerical value: "))
if user_val < 0:
    print("Negative numbers are not allowed")
else:
    result = square_and_multiply(user_val)
    print("The result after taking the square root of the number and multiplying it is:", result)