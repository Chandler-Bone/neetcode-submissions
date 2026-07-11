class Node :
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = next.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            tmp_node = self.left.next
            self.remove(tmp_node)
            del self.cache[tmp_node.key]
        
