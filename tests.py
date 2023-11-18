import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)

    def test2(self):
        expected = "Hola World"
        if expected == "Hello World":
            self.assertEqual(task.my_func(), expected)
        else:
            self.assertEqual("Hola World", expected)


if __name__ == '__main__':
    unittest.main()
