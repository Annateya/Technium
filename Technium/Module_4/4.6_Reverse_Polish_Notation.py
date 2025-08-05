class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)


def rpn(line):
    tokens = line.split(' ')
    for i in tokens:
        if i.isdigit():
            operands.push(i)
        if i in '+-*/':
            a = int(operands.pop())
            b = int(operands.pop())
            if i == '+':
                operands.push(b+a)
            elif i == '-':
                operands.push(b-a)
            elif i == '*':
                operands.push(b*a)
            elif i == '/':
                operands.push(b/a)
    return operands.peek()



operands = Stack()

my_line = input('Введите выражение:')

print(rpn(my_line))
