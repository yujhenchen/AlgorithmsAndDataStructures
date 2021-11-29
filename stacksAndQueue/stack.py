# last in first out
# where stack is used? 1. managing function invocations, undo redo, routing (the history objects)
# implement stack using array


class Stack(object):
    def __init__(self):
        super().__init__()
        self.data = []
        self.length = 0

    def push(self, value):
        self.data.append(value)
        self.length += 1
        return

    def pop(self):
        if self.length < 1:
            return None
        self.length -= 1
        value = self.data.pop()
        return value
