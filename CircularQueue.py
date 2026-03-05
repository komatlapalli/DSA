class Queue:
    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.top = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ''.join(values)
    
    