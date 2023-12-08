#미완성
class LinearDeque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.lineardeque = [None] * capacity
        self.front = -1 
        self.rear = -1  

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def addrear(self, item):
        if self.is_full():
            print("덱이 가득 찼습니다.")
        else:
            self.rear += 1
            self.lineardeque[self.rear] = item

    def addfront(self, item):
        if self.is_full():
          print("덱이 가득 찼습니다.")  
        else:
            
          

    def deleterear(self):
        if self.is_empty():
            print("덱이 비어있습니다.")
        else:
            self.lineardeque[self.front] = None


    def deletefront(self):
        if self.is_empty():
            print("덱이 비어있습니다.")
            return None
        else:
            item = self.lineardeque[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return item

    def getfront(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
            return None
        else:
            return self.lineardeque[self.front]
         
LinearDeque = LinearDeque()
print(LinearDeque.getfront()) 

LinearDeque.addrear(1)
print(LinearDeque.getfront())

LinearDeque.addrear(2)
print(LinearDeque.getfront())  

LinearDeque.addrear(3)
print(LinearDeque.getfront())

LinearDeque.addrear(4)
print(LinearDeque.getfront()) 

LinearDeque.addrear(5)
print(LinearDeque.getfront())

LinearDeque.addrear(6)
print(LinearDeque.getfront())

print(LinearDeque.lineardeque)

LinearDeque.deletefront()
print(LinearDeque.getfront())

