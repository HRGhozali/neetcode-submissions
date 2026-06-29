class MyHashSet:

    def __init__(self):
        self.table = []

    def add(self, key: int) -> None:
        if key not in self.table:
            self.table.append(key)
        return None
        

    def remove(self, key: int) -> None:
        if key in self.table:
            self.table.remove(key)
        return None

    def contains(self, key: int) -> bool:
        return key in self.table


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)