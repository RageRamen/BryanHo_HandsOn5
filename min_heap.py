
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def build_min_heap(self, array):
        self.heap = array
        self.size = len(array)
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.size and self.heap[l] < self.heap[i]:
            smallest = l
        if r < self.size and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def get_min(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def pop_min(self):
        if self.size == 0:
            return None
        min = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return min


# Example using integers
min_heap_int = MinHeap()
print("Min heap with integers:")

test_array = [4, 2, 1, 6, 5, 8, 7, 9, 11, 14]
print("Test array:", test_array)

min_heap_int.build_min_heap(test_array)
print("Min Heap:", min_heap_int.heap)
print("Get min:", min_heap_int.get_min())
print("Pop min:", min_heap_int.pop_min())
print("Heap after popping min:", min_heap_int.heap)

# Example using floats
min_heap_float = MinHeap()
print("\nMin heap with floats:")

test_array = [9.7, 8.9, 1.2, 1.5, 4.2, 7.9, 14.2, 16.7, 13.6, 2.9]
print("Test array:", test_array)

min_heap_float.build_min_heap(test_array)
print("Min Heap:", min_heap_float.heap)
print("Get min:", min_heap_float.get_min())
print("Pop min:", min_heap_float.pop_min())
print("Heap after popping min:", min_heap_float.heap)