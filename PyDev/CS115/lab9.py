# mandelbrot.py
# Lab 9
#
# Name: arana3 - Aparajita Rana

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    """ mult uses only a loop and addition
               to multiply c by the integer n
           """
    result = 0
    for x in range(n):
        result = c + result
    return result

def update(c,n):
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """ inMSet takes in
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
        Then, it should return
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0 + 0j
    for x in range(n):
        z = z**2 + c  
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col,row):
    """ a function that returns True if we want
    """ #the pixel at col, row and False otherwise
    if col%10 == 0  and  row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
    """ #to create and save a png image
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()


def scale(pix, pixMax, floatMin, floatMax):
    return floatMin + ((pix/pixMax)*(floatMax-floatMin))

def mset():
    """creates a 300x200 image of the Mandelbrot set"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            x = scale(col,width,-2.0,1.0)
            y = scale(row,height,-1.0,1.0)
            c= x + y*1j
            if inMSet(c,25) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
    
print(update(1,3))
print(mult(6,7))
c = 0 + 0j # this one is in the set
print(inMSet(c, 25))
test()
print(scale(100, 200, -2.0, 1.0))
mset()