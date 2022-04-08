# Write a function that takes amount-in-dollars and amount-to-rupee conversion price, it then returns the amount converted to rupees. Create the function in both void and non-void forms.
def void(amount: float | int, conPrice: float | int):
    print(f'In Void form Rs: {amount*conPrice}')


def non_void(amount: float | int, conPrice: float | int) -> float:
    return amount*conPrice


# Write a function to calculate volume of a box with appropriate default values for its parameters.Your function should have the following input parameters: (a) length of box; (b) width of the box; (c) height of the box.
def VolCalc(length: float | int, width: float | int, height: float | int) -> float | int:
    return length*width*height


# WAP to have the following functions:
'''
(i) a function that takes a number as argument and calculates cube for it.The function does not return a value. If there is no value passes to the function in function call, the function should calculate cube of 2.
(ii) a function that takes two char arguments and returns True if both the arguments are equal otherwise false.
'''
# Test both these functions by giving appropriate function call statements


def Cuber(val: int | float = 2):
    cube = val**3


def CharCheck(val1: chr, val2: chr) -> bool:
    if val1 == val2:
        return True
    else:
        return False


print(Cuber())  # argument without val
print(Cuber(3))  # argument with value
print(CharCheck('a', 'b'))  # checking char


# Write a function that receives two numbers and generates a random number from that range.Using this function, the main program should be able to print three numbers randomly.
def rand(startVal: int, endVal: int) -> int:
    from random import randint
    return randint(startVal, endVal)

# Write a function that receives two string arguments and checks whether they are same-length strings (return True in this case otherwise False)


def StringCheck(args1: str, args2: str):
    if len(args1) == len(args2):
        return True
    else:
        return False


# Write a function namely 'nthRoot()' that receives two parameters x and n and returns nth root of x, i.e., x^(1/n). The defualt value of n is 2
def nthRoot(x: int | float, n: int | float = 2) -> float | int:
    return x**(1/n)


# Write a function that takes a number and then returns a randomly generated number having exactly n digits (Not starting with zero) eg., if n is 2 then function can randomly return a number from 10-99,but 07,02 are not valid two digit numbers.
def RandDigits(n: int) -> int:
    from random import randrange
    return randrange(10**(n-1), 10**(n))

# Write a function that takes two numbers and returns the number that has minimum one's digit.
# [For example, if numbers passed are 491 and 728, then the function will return 491 because it has  got minimum one's digit out of the two given numbers (491's 1 < 278's 8)].


def minOneDigit(num1: int, num2: int) -> int | tuple:
    if num1 % 10 > num2 % 10:
        return num2
    elif num1 % 10 < num2 % 10:
        return num1
    else:
        return num1, num2


# WAP  that  generates a series using a function which takes first and last values of the series and then generates four terms that are equidistant eg: if two numbers passed are 1 and 7 then  function returns 1 3 5 7.
def seriesGen(startInd: int, endInd: int) -> list:
    dist = (startInd+endInd)//4
    terms = []
    for i in range(startInd, endInd+1, dist):
        if len(terms) == 4:
            break
        terms.append(i)
    if terms[3] == endInd:
        return terms
