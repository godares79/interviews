# Playing around with types of linked lists.
from typing import Optional


class SinglyLinkedList:
    """A singly linked list with only a head pointer."""

    class ListItem:
        def __init__(self, value=None):
            self.value = value
            self.next = None

        def __str__(self):
            return "{} ({})".format(self.value, hash(self))

    def __init__(self):
        self.head = None

    def __str__(self):
        items = []
        if not self.head:
            return items

        items.append(str(self.head))
        next_item = self.head.next
        while next_item:
            items.append(str(next_item))
            next_item = next_item.next

        return " -> ".join(items)

    def __len__(self):
        length = 0
        item = self.head
        while item:
            item = item.next
            length += 1
        return length

    def add_to_head(self, item: ListItem):
        if not item:
            return

        if not self.head:
            self.head = item
            self.head.next = None
        else:
            item.next = self.head
            self.head = item

    def remove_head(self) -> Optional[ListItem]:
        if not self.head:
            return None

        item_to_return = self.head
        self.head = item_to_return.next
        return item_to_return

    def add_to_tail(self, item: ListItem):
        """Because there is only a head pointer, traverse the list first.

        Naturally, to speed up this process could keep a tail pointer.
        """
        if not item:
            return
        if not self.head:
            self.head = item
            return

        next_item = self.head.next
        while next_item:
            if not next_item.next:
                next_item.next = item
                return
            next_item = next_item.next

    def get_tail(self) -> Optional[ListItem]:
        if not self.head:
            return None

        item = self.head
        while item.next:
            item = item.next
        return item


class DoublyLinkedList:
    """A doubly linked list."""

    class ListItem:
        def __init__(self, value=None):
            self.value = value
            self.next = None
            self.prev = None

        def __str__(self):
            return "{} ({})".format(self.value, hash(self))

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        items = []
        if not self.head:
            return items

        items.append(str(self.head))
        next_item = self.head.next
        while next_item:
            items.append(str(next_item))
            next_item = next_item.next

        return " <-> ".join(items)

    def __len__(self) -> int:
        length = 0
        item = self.head
        while item:
            item = item.next
            length += 1
        return length

    def __contains__(self, item):
        item_to_check = self.head
        while item_to_check:
            if item == item_to_check:
                return True
            item_to_check = item_to_check.next
        return False

    def add_to_head(self, value: ListItem):
        if not self.head:
            self.head = value
            self.tail = value
            return

        value.next = self.head
        self.head.prev = value
        self.head = value

    def add_to_tail(self, value: ListItem):
        if not self.head:
            self.head = value
            self.tail = value
            return

        self.tail.next = value
        value.prev = self.tail
        self.tail = value

    def remove_element(self, value: ListItem):
        """This doesn't actually assume that the value is in the list."""
        if not value:
            raise Exception("The argument must not be None.")

        if value == self.head and value == self.tail:
            self.head = value.next
            self.tail = value.prev
            return
        elif value == self.head:
            value.next.prev = None
            self.head = value.next
            return
        elif value == self.tail:
            value.prev.next = None
            self.tail = value.prev
            return
        else:
            if not value.prev or not value.next:
                # If we reach this point and the input value doesn't have a
                # previous or next, then it is
                raise Exception(
                    "The input item is malformed, is it a part of this list?"
                )
            value.prev.next = value.next
            value.next.prev = value.prev
