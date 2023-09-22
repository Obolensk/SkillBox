# TODO здесь писать код

my_stack = {}
todoist = []

class Stack:
    pass

class TaskManager():

    def new_task(self, task, priority):
        if priority in my_stack.keys():
            my_stack[priority] += '; ' + task
        else:
            my_stack[priority] = task

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

for i in sorted(my_stack.keys()):
    print(i, ':', my_stack[i])

