# first in first out
# use: background tasks, download files, print- tasks processing
class Queue(object):
    def __init__(self):
        super().__init__()
        self.data = []
        self.length = 0

    def push(self, value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        if self.length < 1:
            return None
        self.length -= 1
        return self.data.pop(0)
