import pytest
import L2_final

def test_L2_types():
    with pytest.raises(TypeError):
        L2_final.L2([-3, 'c'])
        
    with pytest.raises(ValueError):
        L2_final.L2([3, 4], [1])