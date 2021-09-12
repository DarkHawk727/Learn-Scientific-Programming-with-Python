from OneBasedList import OneBasedList
import unittest

class TestOneBasedList(unittest.TestCase):
    def test_assignment(self):
        lst0 = ['a', 'b', 'c']
        lst1 = OneBasedList(lst0)
        self.assertEqual(str(lst1), str(lst0))
        self.assertEqual(lst1[1], 'a')
        self.assertEqual(lst1[3], 'c')
        self.assertRaises(IndexError, lst1.__getitem__, 0)

        self.assertEqual(lst1[-1], lst0[-1])
        self.assertEqual(lst1[-3], lst0[-3])
        self.assertRaises(IndexError, lst1.__getitem__, -4)

    def test_slices(self):
        lst0 = list('abcdef')
        lst1 = OneBasedList('abcdef')
        self.assertEqual(lst0[1:3], lst1[2:3])
        self.assertEqual(lst0[1:], lst1[2:])
        self.assertEqual(lst0[1:6:2], lst1[2:6:2])
        self.assertEqual(lst0[:6], lst1[1:6])
        self.assertEqual(lst0[:], lst1[:])
        self.assertRaises(IndexError, lst1.__getitem__, slice(0,1))
        self.assertEqual(lst0[-1:1:-1], lst1[-1:2:-1])
        self.assertEqual(lst0[5:1:-2], lst1[6:2:-2])

        self.assertRaises(IndexError, lst1.__setitem__, 0, 'x')
        lst0[0] = 'z'
        lst1[1] = 'z'
        self.assertEqual(lst0, lst1)
        lst0[-1] = 'q'
        lst1[-1] = 'q'
        self.assertEqual(lst0, lst1)

        lst0[1:4] = 'STU'
        lst1[2:4] = 'STU'
        self.assertEqual(lst0, lst1)
        lst0[-2::-1] = [1,2,3,4,5]
        lst1[-2::-1] = [1,2,3,4,5]
        self.assertEqual(lst0, lst1)

        lst2 = lst1[:]
        self.assertEqual(type(lst2), OneBasedList)
        lst2 = lst1[1:3]
        self.assertEqual(type(lst2), OneBasedList)

        lst3 = OneBasedList('ABCDEFGHIJKL')
        self.assertEqual(lst3[3:11:4], ['C','G','K'])
        self.assertEqual(lst3[::3], ['A', 'D','G','J'])
        self.assertEqual(lst3[::-3], ['L', 'I','F','C'])

    def test_delete_items(self):
        lst0 = list('abcdef')
        lst1 = OneBasedList('abcdef')
        del lst0[3]
        del lst1[4]
        self.assertEqual(lst0, lst1)
        del lst0[2:]
        del lst1[3:]
        self.assertEqual(lst0, lst1)

    def test_equality(self):
        lst0 = list('ABCD')
        lst1 = OneBasedList('ABCD')
        self.assertEqual(lst1, lst1)
        self.assertEqual(lst0, lst1)
        lst2 = OneBasedList('ABCDE')
        lst2.pop()
        self.assertEqual(lst1, lst2)

    def test_index(self):
        lst1 = OneBasedList('abcd')

        self.assertEqual(lst1.index('a'), 1)
        self.assertRaises(ValueError, lst1.index, 'z')

        lst2 = OneBasedList('abcdefabcdef')
        self.assertEqual(lst2.index('a', 6), 7)
        self.assertEqual(lst2.index('a', 6, 7), 7)

    def test_pop(self):
        lst1 = OneBasedList('abcdefgh')
        lst1.pop()
        self.assertEqual(lst1, list('abcdefg'))
        lst1.pop(3)
        self.assertEqual(lst1, list('abdefg'))

    def test_copy(self):
        lst1 = OneBasedList('abcdefgh')
        lst2 = lst1.copy()#[:]
        self.assertEqual(type(lst2), OneBasedList)

    def test_clear(self):
        lst = OneBasedList('ABCD')
        lst.clear()
        self.assertEqual(type(lst), OneBasedList)

    def test_insert(self):
        lst0 = list('ABCD')
        lst1 = OneBasedList('ABCD')
        lst0.insert(1, 'z')
        lst1.insert(2, 'z')
        self.assertEqual(lst0, lst1)
        lst0.insert(-1, 'q')
        lst1.insert(-1, 'q')
        self.assertEqual(lst0, lst1)

    def test_concatenate(self):
        lst1 = OneBasedList('abcd')
        lst2 = OneBasedList('efgh')
        self.assertEqual(lst1 + lst2, list('abcdefgh'))
        self.assertEqual(type(lst1 + lst2), OneBasedList)
        self.assertEqual(type(lst1 + [1, 2, 3]), OneBasedList)
        self.assertEqual(type([1, 2, 3] + lst1), list)

        self.assertEqual(lst1*3, list('abcdabcdabcd'))
        self.assertEqual(type(lst1*3), OneBasedList)
        self.assertEqual(2*lst1, list('abcdabcd'))
        self.assertEqual(type(2*lst1), OneBasedList)

    def test_extend(self):
        lst1 = OneBasedList('abcd')
        lst2 = OneBasedList('efgh')
        lst1.extend(lst2)
        self.assertEqual(lst1, list('abcdefgh'))
        self.assertEqual(type(lst1), OneBasedList)

unittest.main()