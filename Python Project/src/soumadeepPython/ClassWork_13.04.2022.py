# WAP with functions: 1) manip(str,p) with one String argument and one integer argument.It displays the characters of even positions of String, if p is an even number otherwise, it displays the characters of odd positions. 2) manip(a,ch) with one integer argument and one character argument. It computes the square root of the integers, if ch is 's', else it computes the cube root of the integers.
def manip(str: str, p: int) -> chr:
    if p % 2 == 0:
        for i in range(len(str), 2):
            print(str[i], end=' ')
    else:
        for i in range(1, len(str), 2):
            print(str[i], end=' ')


def _manip(a: int, ch: chr) -> int | float:
    if ch is 's':
        print("Sqauer Root: ", a**2)
    else:
        print("Cube root: ", a**3)


manip("Hello", 2)
_manip(3, 's')


# WAP with functions: 1) compare(int,int): to compare two integers values and print the greater of the two integers. 2) compare(char,char): to compare the numeric value of two characters and print with the higher numeric value. 3)compare(String,String): to compare the length of the two strings and point the longer of the two.
def compare(a: int, b: int):
    if a > b:
        print(f'{a} is greater')
    else:
        print(f'{b} is greater')


def _compare(a: chr, b: chr):
    if a > b:
        print(f'{a} is greater')
    else:
        print(f'{b} is greater')


def __compare(a: str, b: str):
    if a > b:
        print(f'{a} is greater')
    else:
        print(f'{b} is greater')


compare(2, 3)
_compare('a', 'A')
__compare("Hello", "Python")


# WAP with functions: 1) polygon(n,ch): with one integer and one character type argument to draw a filled square of side n using the character stored in ch. 2) polygon(x,y): with two integer arguments that draws a filled rectangle of length x and breadth y,using the symbol '@'. 3) polygon(): with no argument that draws a filled triangle as shown:
'''
*
**
***
'''


def polygon(n: int, ch: chr):
    for i in range(n):
        if i == 0 or i == n-1:
            print(ch*n)
        else:
            print(ch, ' '*(n-2)+ch)


def _polygon(x: int, y: int):
    for i in range(y):
        if i == 0 or i == y-1:
            print('@'*x)
        else:
            print('@'+' '*(x-2)+'@')


def __polygon():
    for i in range(1, 4):
        print('*'*i)


polygon(4, 's')
_polygon(5, 3)
__polygon()
