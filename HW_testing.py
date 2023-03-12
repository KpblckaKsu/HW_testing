# Нужно реализовать класс Stack со следующими методами:
# is_empty — проверка стека на пустоту. Метод возвращает True или False;
# push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
# pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
# peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
# size — возвращает количество элементов в стеке.

class Stack:
    def __init__(self):
        self.list_data = []

    def is_empty(self):
        if len(self.list_data) == 0:
            res = True
        else:
            res = False
        return res

    def push(self, new_element):
        self.list_data.append(new_element)

    def pop(self):
        self.list_data.pop()

    def peek(self):
        res = self.list_data[-1]
        return res

    def size(self):
        res = len(self.list_data)
        return res

    def parenthesis_balance_brackets(self, brackets_str):
        result = True
        for i in brackets_str:
            if i in '({[':
                self.push(i)
            elif i in ')}]':
                if self.is_empty():
                    result = False
                    break
                last_element = self.list_data.pop()
                if last_element == '(' and i == ')' or last_element == '{' and i == '}' \
                        or last_element == '[' and i == ']':
                    continue
                else:
                    result = False
                    break
        if result and self.is_empty():
            print('Сбалансированно')
        else:
            print('Несбалансированно')


list_brackets = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
for elm in list_brackets:
    new_ex = Stack()
    new_ex.parenthesis_balance_brackets(elm)

