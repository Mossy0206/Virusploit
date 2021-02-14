



class empl:
    numOfEmps = 0
    raisAmt = 1.01
    def __init__(self, first, last, pay):
        self.fnam = first
        self.lnam = last
        self.pay = pay
        self.email = (first + '.' + last + '@gmail.com')
        empl.numOfEmps += 1
    def fulname(self):
        return '{} {}'.format(self.fnam, self.lnam)
        #return (self.fnam + ' ' + self.lname
    def apply_raise(self):
        self.pay = (self.pay * self.raisAmt)
        return ''

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raisAmt = amount

    @classmethod
    def from_string(cls, empSTR):
        first, last, pay = empSTR1.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
mydate = datetime.date(2021, 10, 2)
print(empl.is_workday(mydate))


#emp1 = empl('Alex', 'Moss', 60000)
#emp2 = empl('Test', 'User', 50000)
#emp3 = empl('test2', 'Mossy', 30000)
#
#empSTR1 = 'bilbo-baggins-1000000'
#empSTR2 = 'bob-cratchit-2000000'
#empSTR3 = 'ben-fallow-3000000'
#newemp1 = empl.from_string(empSTR1)
#print(newemp1.fulname())
#print(newemp1.email)



#empl.set_raise_amt(1.05)

#print (empl.raisAmt)
#print (emp1.raisAmt)
#print (emp2.apply_raise(), end='')
#print (emp2.pay)
#print (empl.numOfEmps)
#print (emp2.fulname())


