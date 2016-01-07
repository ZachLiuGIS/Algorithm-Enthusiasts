class MaxPQ(object):
    class Empty(Exception):
        pass

    def __init__(self):
        self._heapList = [None]

    def size(self):
        return len(self._heapList) - 1

    def is_empty(self):
        return self.size() == 0

    def insert(self, v):
        self._heapList.append(v)
        self.swim(self.size())

    def peek_max(self):
        if not self.is_empty():
            return self._heapList[1]
        else:
            raise self.Empty

    def del_max(self):
        if not self.is_empty():
            max_value = self._heapList[1]
            size = self.size()
            self._heapList[1] = self._heapList[size]
            del self._heapList[size]
            self.sink(1)
            return max_value
        else:
            raise self.Empty

    def swim(self, i):
        while i > 1 and self._heapList[i] > self._heapList[int(i / 2)]:
            self._heapList[i], self._heapList[int(i / 2)] = self._heapList[int(i / 2)], self._heapList[i]
            i = int(i / 2)

    def sink(self, i):
        while i * 2 <= self.size():
            j = i * 2
            if j < self.size() and self._heapList[j] < self._heapList[j + 1]:
                j += 1
            if self._heapList[i] >= self._heapList[j]:
                break
            self._heapList[i], self._heapList[j] = self._heapList[j], self._heapList[i]
            i = j


class MinPQ(object):
    class Empty(Exception):
        pass

    def __init__(self):
        self._heapList = [None]

    def size(self):
        return len(self._heapList) - 1

    def is_empty(self):
        return self.size() == 0

    def insert(self, v):
        self._heapList.append(v)
        self.swim(self.size())

    def peek_min(self):
        if not self.is_empty():
            return self._heapList[1]
        else:
            raise self.Empty

    def del_min(self):
        if not self.is_empty():
            max_value = self._heapList[1]
            size = self.size()
            self._heapList[1] = self._heapList[size]
            del self._heapList[size]
            self.sink(1)
            return max_value
        else:
            raise self.Empty

    def swim(self, i):
        while i > 1 and self._heapList[i] < self._heapList[int(i / 2)]:
            self._heapList[i], self._heapList[int(i / 2)] = self._heapList[int(i / 2)], self._heapList[i]
            i = int(i / 2)

    def sink(self, i):
        while i * 2 <= self.size():
            j = i * 2
            if j < self.size() and self._heapList[j] > self._heapList[j + 1]:
                j += 1
            if self._heapList[i] <= self._heapList[j]:
                break
            self._heapList[i], self._heapList[j] = self._heapList[j], self._heapList[i]
            i = j


if __name__ == '__main__':
    max_q = MaxPQ()
    for v in [6, 10, -2, 20, 9, 3, -8, 16, 11, 2]:
        max_q.insert(v)
    print(max_q.peek_max())

    min_q = MinPQ()
    for v in [6, 10, -2, 20, 9, 3, -8, 16, 11, 2]:
        min_q.insert(v)
    print(min_q.peek_min())

