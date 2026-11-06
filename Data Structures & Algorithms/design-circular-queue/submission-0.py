class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.count = 0

        self.head = ListNode()
        current = self.head

        for i in range(1, k):
            current.next = ListNode()
            current = current.next

        current.next = self.head
        self.rear = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head.val = value
            self.rear = self.head
        else:
            self.rear = self.rear.next
            self.rear.val = value

        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.count -= 1

        if self.isEmpty():
            self.rear = self.head

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()