def sum_digits(A):
    '''
    takes a list A, and returns
    the sum of all the digits in the
    list e.g. [10, 30, 45] should return 1 + 0 + 3 + 0+4 +5
    '''
    total = 0

    for i in A:
        g = str(i)
        for x in g:
            v = int(x)
            total += v
    return total


# test tour code

print sum_digits([10, 30, 45])
