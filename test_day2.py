import pytest

from day2 import generate_invalid_ids_v2

def test_generate_invalid_ids_v2():
    ids = generate_invalid_ids_v2(998, 1111)
    expected_ids = {999, 1010, 1111}

    assert ids == expected_ids