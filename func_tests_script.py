import sys
import argparse
import os
import numpy as np
import data_processor as dpr


def main():
    parser = argparse.ArgumentParser(description='Enter test type.')

    parser.add_argument('--test_type',
                        type=str,
                        help='random_matrix, file_dims, or write_matrix',
                        required=True)

    args = parser.parse_args()
    test_type = args.test_type

    # create toy data
    np.random.seed(2)
    matrix = np.random.rand(3, 3)
    toy_file = 'toy_file.csv'
    np.savetxt(toy_file, matrix, delimiter=',')

    if test_type == 'random_matrix':
        dpr.get_random_matrix(3, 3)

    if test_type == 'file_dims':
        dpr.get_file_dimensions(toy_file)

    if test_type == 'write_matrix':
        dpr.write_matrix_to_file(3, 3, 'test_data.csv')

    # delete files created
    os.remove('toy_file.csv')
    os.remove('test_data.csv')
