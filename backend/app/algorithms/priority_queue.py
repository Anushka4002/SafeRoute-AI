import heapq


class PriorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0