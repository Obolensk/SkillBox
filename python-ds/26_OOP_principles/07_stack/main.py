# TODO здесь писать код

my_stack = {}

class Stack:

    # def add_the_task(self):
    #     my_stack

    def del_the_task(self):
        pass


class TaskManager(Stack):
    def __init__(self, stack):
        self.stack = stack

    def new_task(self, task, priority):
        my_stack[priority] = task
        # self.stack.add_the_task(task)


print(my_stack)

print(my_stack)