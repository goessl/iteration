from iteration import *
import pytest



def test_sum_default():
    a = [1, 2, 3, 4]
    
    assert sum_default([]) == 0
    assert sum_default([], default=2) == 2
    assert sum_default(a, initial=5) == 15
    with pytest.raises(TypeError):
        sum_default([], initial=MISSING, default=MISSING)

def test_prod_default():
    a = [1, 2, 3, 4]
    
    assert prod_default([]) == 1
    assert prod_default([], default=2) == 2
    assert prod_default(a, initial=5) == 120
    with pytest.raises(TypeError):
        prod_default([], initial=MISSING, default=MISSING)

def test_sumprod_default():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8, 9]
    
    assert sumprod_default([], []) == 0
    assert sumprod_default([], [], default=2) == 2
    assert sumprod_default(a, b, initial=10) == 80
    with pytest.raises(TypeError):
        sumprod_default([], [], initial=MISSING, default=MISSING)
