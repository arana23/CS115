'''
Created on 11/24/18
@author:   arana3    - Aparajita Rana
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
    whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day
    
    def tomorrow(self):
        #represents one day after the date it originally was
        days = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31,days,31,30,31,30,31,31,30,31,30,31)
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1
    
    def yesterday(self):
        #represents one day before the date it originally was
        days = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31,days,31,30,31,30,31,31,30,31,30,31)
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year += -1
            else:
                self.day = DAYS_IN_MONTH[self.month-1]
                self.month += -1
        else:
            self.day += -1 
    
    def addNDays (self, N):
        # N days after the date it originally was
        print(self)
        for days in range (N):
            self.tomorrow()
            print (self)
            
    def subNDays (self, N):
        # N days before the date it originally was
        print(self)
        for days in range(N):
            self.yesterday()
            print(self)
            
    def isBefore (self, d2):
        #Decides whether self is before d2
        if self.year > d2.year :
            return False
        elif self.year < d2.year:
            return True
        elif self.month > d2.month:
            return False
        elif self.month < d2.month:
            return True
        elif self.day > d2.day:
            return False
        elif self.day < d2.day:
            return True
        else:
            return False

    def isAfter (self, d2):
        #check if val is after the give d2
        if self.isBefore(d2):
            return False
        elif d2.isBefore(self):
            return True
        else:
            return False

    def diff (self, d2):
        #Return num representing the number of days
        day1 = self.copy()
        day2 = d2.copy()
        count = 0
        while day1.isBefore(day2):
            count += -1
            day1.tomorrow()
        while day1.isAfter(day2):
            count += 1
            day1.yesterday()
        return count

    def dow(self):
        #Indicates the day of the week of the object
        x = Date(12, 7, 1941)
        DaysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
        return DaysOfWeek[self.diff(x)%7]   
    