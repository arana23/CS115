def dbl(value):
    return value+32

def dbl2(value2):
    return value2-32

def dbla(cf):
    return (9/5)*value

def dblb(fc):
    return (5/9)*value2

def fahrenheit(celsius):
    """returns the input celsius degrees to fahreinheit"""
    return 9/5*(celsius+32)

def celsius(fahrenheit):
    return 5/9*(fahrenheit-32)

""" Call the functions below the function definitions """

c = float(input('Enter degrees in Celsius: '))
f= fahrenheit(c)
" You can print multiple items in one statment. If you put a comma after each # item " \
"it prins a space and then oes on to print the next item"

print(c,'C =', f, 'F')
print('X.2f F= %, 2f C' % (f,c))

""" %d -> int, %f -> float, %s -> str"""

f=float(input('Enter degrees in Fahrenheit: '))
c=celsius(f)
print('X.2f F= %, 2f C' % (f,c))
print(f,'F =', c, 'C')

"""Converting a Fahrenheit temp to Celsius and back """
print() #print blank line
"""User assert to  check the returned value is equal to the expected value"""
f=float(input('Enter degrees in Fahrenheit: '))

assert fahrenheit(celsius(f)) == f
