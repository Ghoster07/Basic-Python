"""
BASIC OPERATORS and CONTROL FLOW:

ARIMETIC OPERATORS

In boolean, True = 1 and False = 0
"""
print(True + False)
print(False / True)
print(True ** False)

"""
FLOOR DIVISIONS
When using numbers with decimals,a floor division can still return a float number
"""
print(4.5//3.7)
print(-9//4)

"""
Order of operation
PEMDAS
Parenthesis, Exponent, Multiplication Division and Modulus, Addition and Subtraction
"""

"""
LOGICAL OPERATORS
Bitwise logical operators such as:
&, |, ~

are a substitiute for:
and, or, not

But the bitwise one can do some funny things. ^ is exclusive or (XOR), the oppsite of |

"""

"""
ORDER OF LOGICAL OPERATORS
Order of precedence from higher to lower

~, &, ^, |, not, and, or
"""
print(not 7 == 2 or 3 < 1)

result1 = not (5 >= 5 or 3<7)
result2 = not 5 >= 5 and not 3<7
print(result1 == result2)


"""
CONTROL FLOW

This is pretty much the use of if, elif, else statements.

"""

print('We\'re done')

num = 11

if num <= 10:
    num += 11
    print(f"num: {num}")
# chaining off of the `if` above
elif num <= 20:
    num += 5
    # this if is nested
    if num > 20:
        print("num started out as less than or equal to 20 and now num is greater than 20")
    # chaining off of the `if` directly above
    else: 
        print("num is less than 20")
else:
    print("num is greater than 20")


menu_choice = input('Choose a food item: \nBurrito: (b), Pizza: (p), Sandwich: (s): ')

if menu_choice == 'b':
    menu_choice = input('Choose what kind of Burrito you\'d like: Bean and cheese: (a), Breakfast: (b)')
    if menu_choice == 'a': print('You\'ll get a Bean and cheese Burrito')
    elif menu_choice == 'b': print('You\'ll get a Breakfast Burrito')
    else: print('We don\'t have that, sorry we\'re a crappy restaurant')

elif menu_choice == 'p':
    menu_choice = input('Choose what kind of Pizza you\'d like: Cheese: (a), Pepperoni: (b)')
    if menu_choice == 'a': print('You\'ll get a Cheese Pizza')
    elif menu_choice == 'b': print('You\'ll get a Pepperoni Pizza')
    else: print('We don\'t have that, sorry we\'re a crappy restaurant')

elif menu_choice == 's':
    menu_choice = input('Choose what kind of Sandwich you\'d like: Ham: (a), PB&J: (b)')
    if menu_choice == 'a': print('You\'ll get a Ham Sandwich')
    elif menu_choice == 'b': print('You\'ll get a PB&J Sandwich')
    else: print('We don\'t have that, sorry we\'re a crappy restaurant')

else: print('We don\'t have that, sorry we\'re a crappy restaurant')

def is_divisible_by(num, divisor1, divisor2):
    if 0 == num % divisor1 and 0 == num % divisor2:
        print(f"This number is divisible by {divisor1} and {divisor2}")

