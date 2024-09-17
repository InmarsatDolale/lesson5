from datetime import date


class Task:
    def __init__(self, description, due_date, status):
        self.description = description
        self.due_date = due_date
        self.status = status


    def get_description(self):
        return self.description

    def get_due_date(self):
        return self.due_date

    def get_status(self):
        if self.status == 'Выполнено':
            return 'Задача уже выполнена.'
        elif self.status == 'Не выполнено':
            return 'Задача не выполнена'


task1 = Task('Организация хранения', f'{date(2024,8,2)}', 'Выполнено')
task2 = Task('Сделать домашнее задание', f'{date(2024, 9, 1)}', 'Не выполнено')
task3 = Task('Чистка кухни', f'{date(2024, 9, 1)}', 'Не выполнено')
task4 = Task('Садовые работы', f'{date(2024, 9, 1)}', 'Выполнено')


print(task1.get_description())
print(task1.get_due_date())
print(task1.get_status())

print(task2.get_description())
print(task2.get_due_date())
print(task2.get_status())

print(task3.get_description())
print(task3.get_due_date())
print(task3.get_status())

print(task4.get_description())
print(task4.get_due_date())
print(task4.get_status())











