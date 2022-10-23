import unittest
import os
import sys
import numpy as np
import pandas as pd
import filecmp as flc
sys.path.append('../')
import data_processor as dpr # nopep8


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = np.random.seed(2)
        cls.matrix = np.random.rand(5,5)
        cls.toy_data = pd.read_csv('toy_data.csv', sep=',', header=None)
        cls.dims = cls.toy_data.shape
        cls.toy_file = np.savetxt('toy_file.csv', cls.matrix, delimiter=',')
        cls.toy_csv = pd.read_csv('toy_file.csv', sep=',', header=None)

    @classmethod
    def tearDownClass(cls):
        cls.seed =None
        cls.matrix = None
        cls.toy_data = None
        cls.dims = None
        cls.toy_file = None
        cls.toy_csv = None

        
    # tests for get_random_matrix()
    def test_get_random_matrix(self):
        # positive test: test that the matrix returned is correct
        dpr_matrix = dpr.get_random_matrix(5,5)
        self.assertIsNone(np.testing.assert_array_equal(dpr_matrix,
                                                        self.matrix))

        # # negative test: test that the matrix returned is wrong
        # self.assertIsFalse(np.not_equal(dpr_matrix, self.matrix))

        # error handling:


    def test_get_file_dimensions(self):
        # positive test: test that the correct dimensions are returned
        self.assertEqual(dpr.get_file_dimensions('toy_data.csv'), self.dims)

        ## negative test: test that the wrong dimensions are returned
        # wrong_dims = (1,1)
        # self.assertNotEqual((dpr.get_file_dimensions('toy_data.csv'),
        #                      wrong_dims)
        
        # error handling: test that FileNotFoundError is handled
        ## why does this work?
        with self.assertRaises(FileNotFoundError):
            dpr.get_file_dimensions('dne.csv')


    def test_write_matrix_to_file(self):
        # positive test: test that the right matrix is written
        dpr.write_matrix_to_file(5, 5, 'test_data.csv')        
        test_data = pd.read_csv('test_data.csv', sep=',', header=None)
        self.assertIsNone(np.testing.assert_array_equal(test_data,
                                                        self.toy_csv))

        # negative test: test that the wrong matrix is written


        # error handling: is wrong file type handled


if __name__ == '__main__':
    unittest.main()
