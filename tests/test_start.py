import pytest
import ex47

def setup():
    print('setup!')

def teardown():
    print('Teardown')

def test_basic():
    print('I ran!', end = '')
