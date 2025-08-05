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

    def check_line(self, line):
        correct_pair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in line:
            if char in correct_pair.keys(): # открывающая скобка
                self.push(char)
                print('Стек', self.items)
            elif char in correct_pair.values(): # закрывающая скобка
                if self.is_empty():
                    return False
                last_symbol = self.pop()
                if correct_pair[last_symbol] != char:
                    return False
        return self.is_empty()




my_stack = Stack()

my_line = input('Введите скобочную последовательность:')
print(my_stack.check_line(my_line))