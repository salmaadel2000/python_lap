import json
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

class newQueue(Queue):
    all_queues = {}

    def __init__(self, name, size):
        super().init()
        self.queue = []
        self.name = name
        self.size = size
        Queue.all_queues[name] = self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException("Queue size exceeded")
        self.queue.append(value)

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    @classmethod
    def save(cls, filename):
        queues_to_save = {}
        for queue_name, queue_instance in cls.all_queues.items():
            queues_to_save[queue_name] = queue_instance.queue
        with open(filename, 'w') as file:
            json.dump(queues_to_save, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            queues_to_load = json.load(file)
            for queue_name, queue_data in queues_to_load.items():
                queue_instance = Queue(queue_name, len(queue_data))
                queue_instance.queue = queue_data
                cls.all_queues[queue_name] = queue_instance

class QueueOutOfRangeException(Exception):
    pass


queue1 = Queue("queue1", 3)
queue2 = Queue("queue2", 2)


queue1.insert(55)
queue1.insert(66)
queue1.insert(77)

queue2.insert(88)
queue2.insert(99)  

print(queue1.is_empty()) 
print(queue2.is_empty())

print(queue1.pop()) 
print(queue2.pop()) 

Queue.save("queues.json")
Queue.load("queues.json")

retrieved_queue1 = Queue.all_queues["queue1"]
print(retrieved_queue1.pop())
