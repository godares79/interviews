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
