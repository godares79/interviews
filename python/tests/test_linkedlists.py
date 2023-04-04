import unittest

import linkedlists


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.llist = linkedlists.SinglyLinkedList()
        self.llist.add_to_head(linkedlists.SinglyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.SinglyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.SinglyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.SinglyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.SinglyLinkedList.ListItem())

    def test_add_to_head(self):
        empty_list = linkedlists.SinglyLinkedList()
        self.assertEqual(None, empty_list.head)

        empty_list.add_to_head(item := linkedlists.SinglyLinkedList.ListItem())
        self.assertEqual(item, empty_list.head)

    def test_add_to_tail(self):
        new_item = linkedlists.SinglyLinkedList.ListItem()
        self.llist.add_to_tail(new_item)
        self.assertEqual(new_item, self.llist.get_tail())  # add assertion here

    def test_get_tail(self):
        empty_list = linkedlists.SinglyLinkedList()
        self.assertEqual(None, empty_list.get_tail())

        empty_list.add_to_head(item := linkedlists.SinglyLinkedList.ListItem())
        self.assertEqual(item, empty_list.get_tail())

    def test_len(self):
        self.assertEqual(5, len(self.llist))


if __name__ == "__main__":
    unittest.main()
