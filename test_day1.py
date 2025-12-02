import pytest

from day1 import turn_dial_v2

#parametrize test cases for turn_dial_v2
@pytest.mark.parametrize("current_location, direction, distance, expected", [
    (50, 'R', 10, (60, 0)),
    (50, 'L', 10, (40, 0)),
    (0, 'L', 5, (95, 0)),
    (0, 'R', 5, (5, 0)),    
    (0, 'R', 100, (0, 1)),
    (0, 'L', 100, (0, 1)),
    (0, 'R', 1000, (0, 10)),
    (52, 'R', 48, (0, 1)),
    (52, 'R', 148, (0, 2)),
    (50, 'R', 60, (10, 1)),
    (10, 'L', 20, (90, 1)),
    (90, 'R', 10, (0, 1)),
    (10, 'L', 10, (0, 1)),
])
def test_turn_dial_v2(current_location, direction, distance, expected):
    actual = turn_dial_v2(current_location, direction, distance)
    assert actual == expected