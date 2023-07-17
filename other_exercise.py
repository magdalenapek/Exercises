class Employee:

    raise_amount = 1.04
    nums_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.nums_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.nums_of_emps)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))




######### first class function

def square(x):
    return x * x

def my_map(func, arg_list):
    result= []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])
print(squares)

def logger(msg):

    def log_message():
        print('Log:', msg)
    return log_message

log_hi = logger('Hi!')
log_hi



def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}'.format(tag,msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline')
print_h1('Another Headline')

print_p = html_tag('p')
print_p('Test paragraph')


### decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

#def display():
    #print('display function ran')

#decorated_display = decorator_function(display)
#decorated_display()

#to jest to samo co to: (nie trzeba ponownie przypisywać funkcji do zmniennej)

@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name,age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25)
display()