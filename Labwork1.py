#ex1
""""
pi = 3.14
r_string = input("Enter circle radius? ")
r = float(r_string)
area = pi * (r**2)
print(f"Circle area = {area}")
"""

#ex2
""""
degree_string = input("enter the temperature: ")
degree = float(degree_string)
f = degree * 1.8 + 32
print(f"the temperature in F is: {f}")
"""

#ex3
""""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number? "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")
"""

#ex4
"""
def is_perfect(n):
    if n <= 1:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

num = int(input("Enter a number? "))
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")

"""

#ex5
"""
colors = ["Blue", "Yellow", "Orange", "Red", "Black"]
fav_color = input("What is your favorite color? ")
colors_lower = [c.lower() for c in colors]
if fav_color.lower() in colors_lower:
    index = colors_lower.index(fav_color.lower())
    print(f"Your colod is at index {index} in my list")
else:
    print("Sorry, I could not find your color")
"""

#ex6
"""
range1 = list(range(7))
print("range1:", range1)

range2 = list(range(1, 11, 3))
print("range2:", range2)

range3 = list(range(5, 0, -1))
print("range3:", range3)

range4 = list(range(6, -3, -2))
print("range4:", range4)

"""

#ex7
"""
def remove_dollar_sign(s):
    result = ""
    for char in s:
        if char != "$":
            result += char
    return result
"""
"""
def remove_dollar_sign(s):
    return s.replace("$", "")
text1 = "$100.00"
text2 = "$1,000$ USD$"

print(remove_dollar_sign(text1))  # Output: 100.00
print(remove_dollar_sign(text2))  # Output: 1,000 USD
"""

#ex8
"""
def extract_even(l):
     return [x for x in l if x % 2 == 0]
list = [1, 4, 5, -1, 10]
print(extract_even(list)) 
"""

#ex9
"""
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(0))
"""

#ex10
""""
def get_divisors(number):
    number = abs(number) 
    if number == 0:
        return []
    
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(get_divisors(12))  
"""

#ex11
"""
import math


p1 = {"x": 1.0, "y": 2.0}
p2 = {"x": 4.0, "y": 6.0}


dx = p2["x"] - p1["x"]
dy = p2["y"] - p1["y"]

distance = math.sqrt(dx**2 + dy**2)
print(f"Distance = {distance}")  

"""

"""
#ex12
def print_pattern(m, n):
    for row in range(m):
        if row == 0 or row == m - 1:
            print("* " * n)
        else:
            if n == 1:
                print("*")
            else:
                print("* " + "  " * (n - 2) + "*")
print_pattern(4, 5)
"""