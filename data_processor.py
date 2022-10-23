import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):
    '''generate a random matrix of floats

    Parameters
    ----------
    num_rows: number of rows
              integer greater than 0

    num_rows: number of columns
              integer greater than 0

    Returns
    -------
    matrix
        2 dimensional numpy array

    '''
    np.random.seed(2)
    matrix = np.random.rand(num_rows, num_columns)
    
    return matrix

def get_file_dimensions(file_name):
    '''return the dimensions of tabular csv
    
    Parameters
    ----------
    file_name: file name
               csv file name as string
    
    Returns
    -------
    dimensions
        tupule with .csv dimensions
    
    '''
    data = pd.read_csv(file_name, sep = ',', header=None)
    dims = data.shape
    
    return (dims)


def write_matrix_to_file(num_rows, num_columns, file_name):
    '''create a .csv file with a matrix of floats

    Parameters
    ----------
    num_rows: number of rows
              integer greater than 0

    num_rows: number of columns
              integer greater than 0

    file_name: file_name.csv
               .csv file to write matrix in

    Returns
    -------
    csv_file
        csv file with matrix
    
    '''
    matrix = get_random_matrix(num_rows, num_columns)
    csv_file = np.savetxt(file_name, matrix, delimiter=',')

    return csv_file
