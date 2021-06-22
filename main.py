import re
from typing import Any
from collections import deque


class Stack:
    def __init__(self, size=10):
        self.__stack = []
        self.__size = size

    @property
    def empty(self) -> bool:
        return not bool(self.__stack)

    def peek(self) -> Any:
        if not self.empty:
            return self.__stack[-1]

    def pop(self) -> Any:
        if not self.empty:
            return self.__stack.pop()
        raise IndexError

    def push(self, data: Any) -> bool:
        if len(self.__stack) == self.__size:
            return False
        self.__stack.append(data)
        return True

    def __len__(self):
        return len(self.__stack)

    def search_and_extract(self, data: Any):
        stack2 = self.__class__(self.__size)
        while not self.empty:
            x = self.pop()
            if x == data:
                break
            else:
                stack2.push(x)
        while not stack2.empty:
            y = stack2.pop()
            self.push(y)
            return x == data

    def __repr__(self):
        return str(self.__stack)


def balance(expr):
    stack1 = Stack()
    x = '{[('
    y = '}])'
    for i in expr:
        if i in y or i in x:
            if i in x:
                stack1.push(i)
            else:
                if not stack1.empty:
                    z = stack1.peek()
                    if x.find(z) == y.find(i):
                        stack1.pop()
                    else:
                        return False
                else:
                    return False
    return stack1.empty


if __name__ == '__main__':
    que = Stack()
    for i in 'qwerty':
        que.push('hfgf')
        que.push(i)
    print(que)
    print(que.search_and_extract('t'))
    print(que)
    print(balance('{}hhdfghsdgf{}{}{}()('))

    exit(0)
