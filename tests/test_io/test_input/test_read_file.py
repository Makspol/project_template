import unittest
from app.io.input import read_file

RESOURCES = './tests/data/'


class ReadFileTest(unittest.TestCase):
    """
    A class for testing the read_file() function in the app.io.input module.
    For testing, unittest is used.
    """
    path = '../../data/test_file.txt'
    text = 'Some text\ntext'

    @classmethod
    def setUpClass(cls) -> None:

        with open(cls.path, 'w') as file:
            file.write(cls.text)

    def test_TypeError(self):
        self.assertRaises(TypeError, read_file, 15)

    def test_FileNotFoundError(self):
        self.assertRaises(FileNotFoundError, read_file, RESOURCES)

    def test_read_file(self):
        self.assertEquals(self.text, read_file(self.path), f'should be:\n{self.text}')


class ReadFileWithPandas(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
