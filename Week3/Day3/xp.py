class Abs:
    '''The abs() function returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.'''
    def __init__(self, number):
       self.number = number
    def abs_func(self):
        print(abs(self.number))
    
    
class Int:
    '''The int() function converts a number or a string to its equivalent integer.'''
    def __init__(self, number):
       self.number = number
    def int_func(self):
        print(int(self.number))
    
class Input:
    '''The input() function allows user input.'''
    def __init__(self, input_info):
       self.input_info = input_info
    def input_func(self):
        print('your input: ', self.input_info)
    
abs_num = Abs(-7.25)
abs_num.abs_func()
print(abs_num.__doc__)
    
int_num = Int(-7.25)
int_num.int_func()
print(int_num.__doc__)
    
    
input_info = input('input info: ')
input1 = Input(input_info)
input1.input_func()
print(input1.__doc__)
    
#task2
    
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
       return str(self.amount) + ' ' + self.currency + 's'
        
    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return repr(str(self.amount) + ' ' + self.currency + 's')
    
    def __add__(self, other):
        if type(other) == Currency:
            if self.currency == other.currency:
                return self.amount + other.amount
            else: 
                raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
                
        else:
            return self.amount + other
        
    def __iadd__(self, other):
        if type(other) == Currency:
            self.amount += other.amount
            return self
        else:
            self.amount += other
            return self
            
    
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)

c1 += 5
print(c1)
c1 += c2
print(c1)

print(c1 + c3)


    
    