class ListNode:
    def __init__(self, key: int = 0, val: int = 0, next: Optional[ListNode] = None, prev: Optional[ListNode] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.dummyStart = ListNode()
        self.dummyEnd = ListNode()

        self.dummyStart.next = self.dummyEnd
        self.dummyEnd.prev = self.dummyStart

        self.capacity = capacity
        self.keyToNode = dict()

    def _remove(self, key: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            prev = self.keyToNode[key].prev
            next = self.keyToNode[key].next
            prev.next, next.prev = next, prev
            del self.keyToNode[key]

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        value = self.keyToNode[key].val
        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self._remove(key)
        
        newNode = ListNode()
        newNode.val = value
        newNode.key = key
        newNode.prev = self.dummyStart
        newNode.next = self.dummyStart.next
        self.dummyStart.next.prev = newNode
        self.dummyStart.next = newNode

        self.keyToNode[key] = newNode

        if len(self.keyToNode) > self.capacity:
            self._remove(self.dummyEnd.prev.key)
        