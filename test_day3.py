from day3 import find_joltage, find_joltage_v2

def test_find_joltage_v2():
    assert find_joltage_v2([1,2,3,4,5], 2) == 45
    assert find_joltage_v2([1,2,3,4,5], 3) == 345
    assert find_joltage_v2([8,1,1,1,1,1,1,1,1,1,1,1,1,9], 12) == 811111111119