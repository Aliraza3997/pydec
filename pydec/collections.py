
"""collections.py: Collection of common data structures"""

__author__ = "Ali Raza"
__license__ = "MIT"
__version__ = "0.9.0"
__maintainer__ = "Ali Raza"
__email__ = "aliraza3997@gmail.com"
__status__ = "Development"


import heapq


class Heap(list):
    """
    Wrapper around Python's heapq for Object Oriented design.
    """

    def __init__(self, heap=None):
        if heap is None:
            heap = []

        heapq.heapify(heap)
        super(Heap, self).__init__(heap)

    def __repr__(self):
        return 'Heap({})'.format(super(Heap, self).__repr__())

    def push(self, item):
        return heapq.heappush(self, item)

    def pop(self):
        return heapq.heappop(self)

    def pushpop(self, item):
        return heapq.heappushpop(self, item)

    def replace(self, item):
        return heapq.heapreplace(self, item)

    def nlargest(self, n, *args, **kwargs):
        return heapq.nlargest(n, self, *args, **kwargs)

    def nsmallest(self, n, *args, **kwargs):
        return heapq.nsmallest(n, self, *args, **kwargs)


class MaxHeapObj(object):
    """
    Item Object for MaxHeap to inverse the comparisons (using heapq)

    """

    def __init__(self, val):self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


class MinHeap(Heap):
    """
    Min Heap implementation.
    """

    def __init__(self, heap=None):
        super(Heap, self).__init__(heap)


class MaxHeap(Heap):
    """
    Max Heap Implementation.
    """

    def __init__(self, heap=None):
        if heap is not None:
            heap = [MaxHeapObj(x) for x in heap]
            print("Converting heap[i] to MaxHeapObj")

        super(MaxHeap, self).__init__(heap)

    def __repr__(self):
        return 'Heap({})'.format([x.val for x in self])

    def __getitem__(self, i):
        return super(MaxHeap, self).__getitem__(i).val

    def push(self, item):
        heapq.heappush(self, MaxHeapObj(item))

    def pop(self):
        return heapq.heappop(self).val

    def pushpop(self, item):
        return heapq.heappushpop(self, MaxHeapObj(item)).val

    def replace(self, item):
        return super(MaxHeap, self).replace(MaxHeapObj(item))

    def nlargest(self, n, *args, **kwargs):
        return [x.val for x in super(MaxHeap, self).nsmallest(n, *args, **kwargs)]

    def nsmallest(self, n, *args, **kwargs):
        return [x.val for x in super(MaxHeap, self).nlargest(n, *args, **kwargs)]
