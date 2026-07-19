from iteration import *
from itertools import islice, chain
import pytest



def test_raiser():
    assert sum(chain([1, 2, 3], raiser())) == 6
    with pytest.raises(IndexError):
        sum(chain([1, 2, 3], raiser(IndexError)))

def test_group_ordinal():
    iterables = (
        (1, 2, 3),
        [4, 5, 6, 7],
        {8}
    )
    expected = [
        (1, 4, 8),
        (2, 5),
        (3, 6),
        (7,)
    ]
    assert list(group_ordinal(*iterables)) == expected
    #empty case
    assert list(group_ordinal()) == []
