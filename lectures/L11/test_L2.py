import pytest
import L2

def test_L2_types():
    with pytest.raises(TypeError):
        L2.L2([-3, 'c'])
        
    with pytest.raises(ValueError):
        L2.L2([3, 4], [1])