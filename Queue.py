from collections import deque
class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
            self.buffer.appendleft(val)

    def dequeue(self):

        return self.buffer.pop()  

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)                  


q_ob=Queue()
q_ob.enqueue({'company':'Wall Mart','timestamp':'15 apr,11.01 AM','price':131.110}) 
q_ob.enqueue({'company':'Wall Mart','timestamp':'15 apr,11.02 AM','price':131})   
q_ob.enqueue( {'company':'Wall Mart','timestamp':'15 apr,11.03 AM','price':130.5})


print(q_ob.dequeue())
print(q_ob.dequeue())
#print(q_ob.dequeue())
print(q_ob.size())   