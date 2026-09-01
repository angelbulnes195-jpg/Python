# DATA TYPE


# Simple Data Types
"Hello Python"  # String
3.123  # Float
3621  # Integer
True  # Boolean

# Structured Data Type
List = [1, 2, 3, 4, 5]  # List
Tuple = (1, 2, 3, 4, "hello")  # Tuple
set = {1, 2, 3, 4, 5}  # Set
dict = {
'Name': "John",
'Age': 30
}  # Dictionary
print(dict['Name'])




# VARIABLES

age = "30"  
age = "30.5"

# concatenation with +
user_age = "User age is: " + age
print(user_age) 

# concatenation with f-strings
user_age1 = f"User age is: {age}"
print(user_age1)





# OPERATORS


# Arithmetic Operators

add = 5 + 3  # Addition
sub = 5 - 3  # Subtraction
multi = 5 * 3  # Multiplication
div = 5 / 3  # Division / Returns float
expo = 5 ** 3  # Exponentiation
low_div = 5 // 3  # Low Division
mod = 5 % 3  # Modulus

print(add, sub, multi, div, expo, low_div, mod)


# Comparison Operators

equal_to = 5 == 3  # Equal to
different_from = 5 != 3  # Different from
greater_than = 5 > 3  # Greater than
less_than = 5 < 3  # Less than
greater_than_equal_to = 5 >= 3  # Greater than or equal to
less_than_equal_to = 5 <= 3  # Less than or equal to

age = 18
if age >= 18:
    print("Access granted")


# Logical Operators

# And / Or / Not

# Only returns True if both conditions are True / Returns True if at least one condition is True / Returns the opposite of the condition


