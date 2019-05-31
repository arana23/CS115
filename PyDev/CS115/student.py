'''
Created on Nov 12, 2018

@author: arana3 - Aparajita Rana

'''
# a class is a collection of attributes and a set for methods a 
#that change the value of attributes. it's a blueprint for defining obecjts that
#you wish to model in code. A class has a constructor method called __int__
#purpose is to initialize the instance variables of the object being created. 
# two underscore- private, one underscore - protected, none - public
#get without set, but you can't set w/o get
from builtins import property

class Student(object):
    def __init__(self, first_name, last_name, sid, gpa):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__gpa=gpa
    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name=first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name=last_name
    
    def __str__(self):
        return self.__first_name+' '+self.__last_name+'(SID:'+\
            self.__sid+', GPA: '+str(self.__gpa)+')'
        
if __name__=='__main__':
    s1=Student('Brian', 'Borowski', '12345', 4.0)
    print(s1.first_name)
    s1.first_name='Scott'
    print(s1.first_name)
    print(s1)