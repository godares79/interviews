import unittest

import linkedlists


class TestSinglyLinkedList(unittest.TestCase):
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


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.llist = linkedlists.DoublyLinkedList()
        self.llist.add_to_head(linkedlists.DoublyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.DoublyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.DoublyLinkedList.ListItem())
        self.middle_item = linkedlists.DoublyLinkedList.ListItem()
        self.llist.add_to_head(self.middle_item)
        self.llist.add_to_head(linkedlists.DoublyLinkedList.ListItem())
        self.llist.add_to_head(linkedlists.DoublyLinkedList.ListItem())

    def test_len(self):
        self.assertEqual(0, len(linkedlists.DoublyLinkedList()))
        self.assertEqual(6, len(self.llist))

    def test_contains(self):
        self.assertTrue(self.middle_item in self.llist)
        other_item = linkedlists.DoublyLinkedList.ListItem()
        self.assertFalse(other_item in self.llist)

    def test_remove_element(self):
        self.assertTrue(self.middle_item in self.llist)
        self.llist.remove_element(self.middle_item)
        self.assertFalse(self.middle_item in self.llist)

        with self.assertRaises(Exception):
            self.llist.remove_element(None)

        with self.assertRaises(Exception):
            # This is just some random node from somewhere, that isn't actually
            # part of the linked list.
            malformed_node = linkedlists.DoublyLinkedList.ListItem()
            self.llist.remove_element(malformed_node)

        # Check the case of a node being head and/or tail.
        old_head = self.llist.head
        starting_length = len(self.llist)
        self.llist.remove_element(old_head)
        self.assertEqual(self.llist.head, old_head.next)
        self.assertFalse(old_head in self.llist)
        self.assertEqual(starting_length - 1, len(self.llist))

        old_tail = self.llist.tail
        starting_length = len(self.llist)
        self.llist.remove_element(old_tail)
        self.assertEqual(self.llist.tail, old_tail.prev)
        self.assertFalse(old_tail in self.llist)
        self.assertEqual(starting_length - 1, len(self.llist))

        tiny_list = linkedlists.DoublyLinkedList()
        only_item = linkedlists.DoublyLinkedList.ListItem()
        tiny_list.add_to_head(only_item)
        tiny_list.remove_element(only_item)
        self.assertIsNone(tiny_list.head)
        self.assertIsNone(tiny_list.tail)


if __name__ == "__main__":
    unittest.main()
