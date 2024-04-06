class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.is_empty():
            value = self.queue[0]
            del self.queue[0]
            return value
        else:
            print("Trying to pop from an empty queue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.pop())  
print(q.pop())  
print(q.pop())  
print(q.pop())  

print(q.is_empty())
