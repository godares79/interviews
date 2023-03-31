# Playing various data structures.

from collections import deque
from collections import defaultdict
import heapq

def list_comprehensions():
    items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    updated_items = ['Item: {0}'.format(x) for x in items]
    filtered_items = ['Item: {} {}'.format(x, x+'z') for x in items if x == 'a' or x == 'f']


def list_type(mylist: list) -> list:
    mylist.append('added item')
    return mylist


def deque_stuff():
    queue: deque = deque()
    stack: deque = deque()

    # Queue is FIFO
    print('_____QUEUE:_____')
    queue.append('first')
    queue.append('second')
    queue.append('third')
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())

    # Stack in LIFO
    print('_____STACK:_____')
    stack.append('first')
    stack.append('second')
    stack.append('third')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


def dicts():
    regular_dict = {}
    def_dict = defaultdict(list)

    # Working on the regular dictionary.
    regular_dict['1'] = 'hello'
    regular_dict['2'] = 'world'
    regular_dict[3] = 'boss'
    total_string: str = regular_dict['1'] + ' ' + regular_dict['2'] + ' -> ' + regular_dict[3]
    for key, value in regular_dict.items():
        # Remember that you can only use operators on values of the same type.
        # So need to make sure keys are all strings here.
        print(str(key) + ' : ' + value)
    for key in regular_dict.keys():
        print(key)
    for value in regular_dict.values():
        print(value)
    # sorted() accepts any iterable, if I use a dict the sort key will be the dict key
    print(sorted(regular_dict, key=lambda x: str(regular_dict[x])))
    del regular_dict[3]
    print(regular_dict)
    regular_dict.clear()
    print(regular_dict)

    # Default dictionary just sets a default value. Kind of insertdefault() on regular dict.
    def_dict[1].append('value')
    def_dict[2].append('value2')
    print(def_dict)


def heap_tests():
    '''
    Python's heap impl is a min heap. For a max heap, just invert the keys.
    (This assumes keys are ints/floats/some number. For other keys, overwrite
    __lt__ and __gt__).
    '''
    input_list = [1, 4, 2, 9, 3, 4, 10, 8]
    heapq.heapify(input_list)
    print(input_list)


    input_list_inverted = [-x for x in input_list]
    heapq.heapify(input_list_inverted)
    print(input_list_inverted)

    # Do a heapsort with a heap.
    heap_sort_list = []
    heapq.heappush(heap_sort_list, 1)
    heapq.heappush(heap_sort_list, 11)
    heapq.heappush(heap_sort_list, 5)
    heapq.heappush(heap_sort_list, -1)
    heapq.heappush(heap_sort_list, 7)
    heapq.heappush(heap_sort_list, -0.5)
    heapq.heappush(heap_sort_list, 8)
    while len(heap_sort_list) > 0:
       print(heapq.heappop(heap_sort_list))


def dict_comprehensions():
    # Playing around with dictionary comprehensions.
    print("Dictionary Comprehensions")
    keys = [x for x in range(10)]
    my_dict = {x: 'Value: {}'.format(x) for x in keys}
    other_dict = {k: v for (k,v) in my_dict.items() if k < 5}
    print(other_dict)


if __name__ == '__main__':
    dict_comprehensions()

