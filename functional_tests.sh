#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test get_random_matrix
run get_random_matrix python func_tests_script.py --test_type random_matrix
    assert_exit_code 0

# test get_file_dimensions
run get_random_matrix python func_tests_script.py --test_type file_dims
    assert_exit_code 0

# test write_matrix_to_file
run get_random_matrix python func_tests_script.py --test_type write_matrix
    assert_exit_code 0

# test plotter
run plotter python plotter.py
    assert_exit_code 0
