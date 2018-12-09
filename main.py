
class Employee():
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    def fullname(self):
         return '{} {}'.format(self.first_name, self.last_name)




emp_1 = Employee('Thomas', 'Doerig', 'doerig.thomas@gmail.com')
emp_2 = Employee('Patrick', 'Doerig', 'patrick.dorig@gmail.com')


print(emp_1.fullname())
