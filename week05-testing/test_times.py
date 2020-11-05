from times import compute_overlap_time
from times import time_range
from pytest import raises
import pytest

testcases = [
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00"),[]),
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2,60), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2,60), [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] ),
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"), [('2010-01-12 12:00:00')]  )
     ]

@pytest.mark.parametrize("time_range_1,time_range_2,expected", testcases)

def test_overall(time_range_1,time_range_2,expected):
    result = (compute_overlap_time(time_range_1, time_range_2))
    assert result == expected

def test_time_backwards():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

