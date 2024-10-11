#!/usr/bin/python3
'''
A python program to compute minimum operation
'''


def minOperations(n):
    '''
    A method that calculates the fewest numbers of operations
    needed to result in exactly nH characters
    '''
    if n == 1:
        return 0  # No operations needed for 1 H character
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            n //= factor
            operations += factor
        factor += 1
    return operations
