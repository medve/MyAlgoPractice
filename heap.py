class BinaryHeapNode:
    def __init__(self, key, value, *args, **kwargs):
        super(BinaryHeapNode, self).__init__(*args, **kwargs)
        self.key = key
        self. value = value

class BinaryHeap:
    def __init__(self, elements_array = None, *args, **kwargs):
        super(BinaryHeap, self).__init__(*args, **kwargs)
        if elements_array is None:
            self._set_storage([])
        else:
            self.build_heap(elements_array)

    def _set_storage(self, storage):
        self.storage = storage
        self.heap_size = len(self.storage)

    def _add(self,element):
        self.storage.append(element)
        self.heap_size += 1
        return self.heap_size

    def _get_by_idx(self,element_index):
        return self.storage[element_index]

    def _l_idx(self,element_index):
        return element_index*2

    def _r_idx(self,element_index):
        return element_index*2 + 1

    def _p_idx(self, element_index):
        return element_index//2

    def _heapify_down(self, element_idx):
        largest_idx = element_idx
        left_idx = self._l_idx(element_idx)
        right_idx = self._r_idx(element_idx)
        element = self.storage[element_idx]

        #сравниваем элемент с каждым из его детей
        if left_idx < self.heap_size and self.storage[left_idx] > element:
            largest_idx = left_idx
        if (right_idx < self.heap_size 
              and self.storage[right_idx] > self.storage[largest_idx]):
            largest_idx = right_idx

        #если один из детей оказывается больше
        #меняем элемент с наибольшим из детей
        if largest_idx != element_idx:
            (self.storage[element_idx],
                self.storage[largest_idx]) = (self.storage[largest_idx], 
                                                self.storage[element_idx])
            #чиним пирамиду после замены
            self._heapify_down(largest_idx)
        
        

    def _heapify_up(self, element_idx):
        parrent_idx = self._p_idx(element_idx)
        #сравниваем элемент с родителем
        if self.storage[element_idx] > self.storage[parrent_idx]:
            #если родитель оказывается меньше
            #меняем элемент с родителем местами
            (self.storage[element_idx],
                self.storage[parrent_idx]) = (self.storage[parrent_idx],
                                                self.storage[element_index])
            #чиним пирамиду для родителя
            self._heapify_up(parrent_idx)

    def insert(self, element):
        element_index = self._add(element)
        self.heapify(element_index)

    def extract_max(self):
        max_element = self.get_max()
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        self.storage.pop()
        return max_element

    def remove(self,element_index):
        #делаем вес элемента бесконечным
        self.storage[element_index] = 1<<32
        #вызываем heapify_up для него
        self.heapify_up(element_index)
        #удаляем максимальный элемент
        self.extract_max()

    def get_max(self):
        return self._get_by_idx(0)

    def build_heap(self, elements_array=None):
        if elements_array is not None:
            self._set_storage(elements_array)
        for i in reversed(range(len(self.storage)//2)):
            self._heapify_down(i)

    def heap_sort(self, elements_array = None):
        if elements_array is not None:
            self.build_heap(elements_array)
        for i in reversed(range(1,len(elements_array))):
            (self.storage[self.heap_size - 1], 
              self.storage[0]) = (self.storage[0],
                                    self.storage[self.heap_size - 1])
            self.heap_size -= 1
            self._heapify_down(0)

bh = BinaryHeap()
bh.heap_sort([8,1,5,1,3,5,1,6,3,2,54,12,3])
print(bh.storage)