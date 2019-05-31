'''
Created on Nov 14, 2018

@author: arana3 - Aparajita Rana
Pledge: I pledge my honor that I have abided by the Stevens Honor System

'''
import math
#contructors with the three variables, deals with case of potential a==0

class QuadraticEquation(object):
    def __init__(self, a, b, c):
        if a==0:
            raise ValueError('Coefficient \'a\' cannot be 0 in a quadratic equation.')
        else:
            self.__a=a
        self.__b=b
        self.__c=c

#defines property as the private a
    @property
    def a(self):
        return self.__a
    
#defines property as the private b
    @property
    def b(self):
        return self.__b
    
#defines property as the private c
    @property
    def c(self):
        return self.__c
    
# calculators discrim. b^2-4ac making sure to use the actual vals
    def discriminant(self):
        temp=(self.__b)**2
        temp2=4*self.__a*self.__c
        return temp-temp2
 # calculators root with - sign making sure to use the actual vals, if dis is negative, return None    
    def root1(self):
        if self.discriminant()<0:
            return None
        else:
            temp=(-1)*(self.__b)+math.sqrt(self.discriminant())
            temp2=2*(self.__a)
            return temp/temp2
# calculators discrim. b^2-4ac making sure to use the actual vals
    def root2(self):
        if self.discriminant()<0:
            return None
        temp=(-1)*(self.__b)-math.sqrt(self.discriminant())
        temp2=2*(self.__a)
        return temp/temp2
    
    def __str__(self):
        a=b=c=''
        if self.__a>0 and self.__a!=1:
            a=str(self.__a)+'x^2 '
        if self.__b>0 and self.__b!=1:
            if self.__c==0:
                b='+ '+str(self.__b*1.0)+'x'
            else:
                b='+ '+str(self.__b*1.0)+'x '
        if self.__c>0:
            c='+ '+str(self.__c*1.0)
        if self.__a<0:
            if self.__a==-1:
                a='-x^2 '
            else:
                a='- '+str(self.__a*-1.0)+'x^2 '
        if self.__b<0:
            if self.__b==-1:
                b='- x '
            else:
                b='- '+str(self.__b*-1.0)+'x '
        if self.__c<0:
            c='- '+str(self.__c*-1.0)
        if self.__b==0:
            b=''
        if self.__c==0:
            c=''
        if self.__a==1:
            a='x^2 '
        if self.__b==1:
            b='+ x '
        if b=='' and c=='':
            return a+'= 0'
        else:
            return a+b+c+' = 0'
    