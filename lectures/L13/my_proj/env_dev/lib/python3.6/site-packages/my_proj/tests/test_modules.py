import my_proj.modules as m
import numpy as np
import pytest

def test_modules_result():
    assert repr(m.Complex(1, 2)) == '1 + 2i'
    assert repr(m.Complex(3,4) - m.Complex(1,2)) == '2 + 2i'

def test_modules_types():
    with pytest.raises(TypeError):
        m.Complex(1, 2) + 'a'
