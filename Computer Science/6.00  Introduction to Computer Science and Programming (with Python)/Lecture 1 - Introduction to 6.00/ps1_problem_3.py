import unittest


def aux():
    return 2

def main():
    return aux() + 2

if __name__ == '__main__':
    print('main result = ', main())