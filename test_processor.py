import unittest
import os
import sys
import numpy as np
import pandas as pd
import filecmp as flc
sys.path.append('../')
import data_processor as dpr  # nopep8


class TestProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = np.random.seed(2)
        cls.matrix = np.random.rand(5, 5)
        cls.toy_file = 'toy_file.csv'
        np.savetxt(cls.toy_file, cls.matrix, delimiter=',')
        cls.toy_data = pd.read_csv(cls.toy_file, sep=',', header=None)
        cls.dims = cls.toy_data.shape

    @classmethod
    def tearDownClass(cls):
        cls.seed = None
        cls.matrix = None
        os.remove(cls.toy_file)
        cls.toy_file = None
        cls.toy_data = None
        cls.dims = None

    # tests for get_random_matrix()
    def test_get_random_matrix(self):
        # positive test: test that the matrix returned is correct
        dpr_matrix = dpr.get_random_matrix(5, 5)
        self.assertIsNone(np.testing.assert_array_equal(dpr_matrix,
                                                        self.matrix))

        # negative test: test that the matrix returned is wrong
        np.random.seed(7)
        wrong_matrix = np.random.rand(5, 5)
        with self.assertRaises(AssertionError):
            np.testing.assert_array_equal(dpr_matrix, wrong_matrix)

        # error handling:
        with self.assertRaises(TypeError):
            dpr.get_random_matrix(5, 'five')

    def test_get_file_dimensions(self):
        # positive test: test that the correct dimensions are returned
        self.assertEqual(dpr.get_file_dimensions('toy_file.csv'), self.dims)

        # negative test: test that the wrong dimensions are returned
        self.assertNotEqual(dpr.get_file_dimensions('toy_file.csv'), (1, 1))

        # error handling: test that FileNotFoundError is handled
        with self.assertRaises(FileNotFoundError):
            dpr.get_file_dimensions('dne.csv')

    def test_write_matrix_to_file(self):
        # positive test: test that the right matrix is written
        dpr.write_matrix_to_file(5, 5, 'test_data.csv')
        test_data = pd.read_csv('test_data.csv', sep=',', header=None)
        self.assertIsNone(np.testing.assert_array_equal(test_data,
                                                        self.toy_data))
        os.remove('test_data.csv')

        # negative test: test that the wrong matrix is written
        np.random.seed(7)
        wrong_matrix = np.random.rand(5, 5)
        with self.assertRaises(AssertionError):
            np.testing.assert_array_equal(test_data, wrong_matrix)

        # error handling: is wrong file type handled
        with self.assertRaises(TypeError):
            dpr.get_random_matrix(5, 'five')


if __name__ == '__main__':
    unittest.main()
