# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

stack_1 = '123456'

class Stack(list):

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return print(len(self) == 0)

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self,value):
        self.append(value)
        return print(self)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        del self[-1]
        return print(self)

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return print(self[-1])

    # возвращает количество элементов в стеке.
    def size(self):
        return print(len(self))

if __name__ == '__main__':
    stack=Stack(stack_1)
    stack.isEmpty()
    stack.push('7')
    stack.pop()
    stack.peek()
    stack.size()
