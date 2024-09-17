#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.
from datetime import datetime

class Task():
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

    def info(self):
        print(f"Задача - {self.description}")
        print(f"Срок - {self.deadline}")
        print(f"Статус - {self.status}")

list_task = []

def add_task(task):
    list_task.append(task)

def mark_task(task):
    task.status = "выполнена"

def output_list_task(list):
    print("Список задач:")
    for task in list:
        if task.status == "не выполнена":
            print(task.description, ' ', task.deadline, ' ', task.status)

task1 = Task("Сделать домашку", datetime(2024, 9, 19, 23, 30), "не выполнена" )
task1.info()
task2 = Task("Ремонт авто", datetime(2024, 9, 23, 0, 0), "не выполнена" )
task3 = Task("Отправить письмо", datetime(2024, 9, 17, 0, 0), "не выполнена" )


add_task(task1)
add_task(task2)
add_task(task3)
output_list_task(list_task)

mark_task(task1)
output_list_task(list_task)
