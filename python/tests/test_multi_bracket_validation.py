import pytest
from challenges.multi_bracket_validation.multi_bracket_validation import *


def test_valid_data():
    actual1=multi_bracket_validation('(){}')
    actual2=multi_bracket_validation('()[[Extra Characters]]')
    actual3=multi_bracket_validation('({()}')
    actual4=multi_bracket_validation('({()})')
    excepted=True
    assert actual1==excepted
    assert actual2==excepted
    assert actual3==excepted
    assert actual4==excepted

def test_valid_data():
    actual1=multi_bracket_validation('({()}')
    actual2=multi_bracket_validation('({())')
    actual3=multi_bracket_validation('({())))')
    actual4=multi_bracket_validation('({()]')
    excepted=False
    assert actual1==excepted
    assert actual2==excepted
    assert actual3==excepted
    assert actual4==excepted
