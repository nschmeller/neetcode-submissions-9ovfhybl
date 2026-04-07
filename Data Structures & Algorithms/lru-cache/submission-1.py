class Node:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            curr = self.keys[key]

            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            self.head.next.prev = curr
            curr.next = self.head.next

            self.head.next = curr
            curr.prev = self.head

            return curr.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            new = Node(key=key, val=value, nxt=self.head.next, prev=self.head)

            new.next = self.head.next
            self.head.next.prev = new

            new.prev = self.head
            self.head.next = new

            self.keys[key] = new
            if len(self.keys) > self.capacity:
                old = self.tail.prev
                self.tail.prev = old.prev
                old.prev.next = self.tail
                del self.keys[old.key]
        else:
            curr = self.keys[key]
            curr.val = value

            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            self.head.next.prev = curr
            curr.next = self.head.next

            self.head.next = curr
            curr.prev = self.head
            

        
