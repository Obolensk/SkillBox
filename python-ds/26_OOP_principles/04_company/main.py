# TODO здесь писать код

class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # def __str__(self):

class Emloyee(Person):

    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def Salary_Count(self):
        total_salary = self.salary
        print('\nЗарплата {} составила {} рублей'.format(self.name, total_salary))
        # return total_salary

class Manager(Emloyee):
    def __init__(self, name, surname, age, salary=13000):
        super().__init__(name, surname, age, salary)

class Agent(Emloyee):
    def __init__(self, name, surname, age, sales, salary=5000):
        super().__init__(name, surname, age, salary)
        self.sales = sales

    def Salary_Count(self):
        total_salary = self.salary + (self.sales * 0.05)
        print('\nОклад {} рублей\nПлюс 5% от продаж {} рублей\nПолучается {} рублей'.format(self.salary, self.sales, self.sales * 0.05))
        print('Зарплата {} составила {} рублей'.format(self.name, total_salary))
        return total_salary

class Worker(Emloyee):
    def __init__(self, name, surname, age, work_hours=150, salary=100):
        super().__init__(name, surname, age, salary)
        self.work_hours = work_hours

    def Salary_Count(self):
        total_salary = self.salary * self.work_hours
        print('\nПочасовая ставка {} рублей\nУмножить на количество отработанных часов {} часов\nПолучается {} рублей'.format(self.salary, self.work_hours, self.work_hours * self.salary))
        print('Зарплата {} составила {} рублей'.format(self.name, total_salary))
        return total_salary

m1 = Manager('Иван', 'Иванов', 25)
m2 = Manager('Том', 'Смит', 28)
m3 = Manager('Брэд', 'Пит', 32)
# print(m1.Salary_Count())
m1.Salary_Count()
m2.Salary_Count()
m3.Salary_Count()

a1 = Agent('Саша', 'Агапов', salary=100, sales=1000, age=25)
a2 = Agent('Дима', 'Свирин', salary=200, sales=1000, age=25)
a3 = Agent('Денис', 'Денисов', salary=300, sales=1000, age=25)
a1.Salary_Count()
a2.Salary_Count()
a3.Salary_Count()

w1 = Worker('Джим', 'Рон', 35, work_hours=160)
w2 = Worker('Тим', 'Кук', 35, work_hours=170)
w3 = Worker('Стив', 'Джобс', 35, work_hours=180)
w1.Salary_Count()
w2.Salary_Count()
w3.Salary_Count()