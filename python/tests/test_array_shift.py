from challenges.array_shift import __version__
from challenges.array_shift.array_shift import *


def test_version():
    assert __version__ == '0.1.0'

# TEST CASE
def test_case():
    userinput1=[[2,4,6,8], 5]
    userinput2=[[4,8,15,23,42],16]

    exOutput1 = [2,4,5,6,8]
    exOutput2 = [4,8,15,16,23,42]

    assert insertShiftArray(userinput1[0],userinput1[1]) == exOutput1 #Test Case1
    assert insertShiftArray(userinput2[0],userinput2[1]) == exOutput2 #Test Case2

