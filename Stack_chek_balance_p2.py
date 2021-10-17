# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

# Пример сбалансированных последовательностей скобок:

stack_1 = '(((([{}]))))'
stack_2 = '[([])((([[[]]])))]{()}'
stack_3 = '{{[()]}}'
# Несбалансированные последовательности:

stack_4 = '}{}'
stack_5 = '{{[(])]}}'
stack_6 = '[[{())}]'


openList = ["[","{","("]
closeList = ["]","}",")"]

class Stack(list):

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return len(self) == 0

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self,value):
        self.append(value)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        if not self.isEmpty():
            value = self[-1]
            del self[-1]
        return value

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        if not self.isEmpty():
            return print(self[-1])

    # возвращает количество элементов в стеке.
    def size(self):
        return print(len(self))

def check_balance(stack_x):
    stack = Stack()
    # stack = []
    for i in stack_x:
        if i in openList:
            stack.push(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    return stack.isEmpty()

if __name__ == '__main__':
    x =[stack_1,stack_2,stack_3,stack_4,stack_5,stack_6]
    for stack in x:
        if check_balance(stack) == True:
            print(f'{stack} - {"Cбалансировано"}')
        else:
            print(f'{stack} - {"Несбалансированно"}')





