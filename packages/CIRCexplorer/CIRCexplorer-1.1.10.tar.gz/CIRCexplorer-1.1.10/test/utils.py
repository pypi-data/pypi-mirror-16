import os


def compare_file(fn1, fn2):
    '''
    Test if two files are same
    '''
    with open(fn1, 'r') as f1, open(fn2, 'r') as f2:
        content1 = set(f1.readlines())
        content2 = set(f2.readlines())
        return content1 == content2


def check_file(test_f, result_f):
    '''
    Check if files are existed and same
    '''
    print('Check %s file...' % test_f)
    assert os.path.isfile(test_f), 'No %s file' % test_f
    assert compare_file(test_f, result_f), 'Difference in %s' % test_f
