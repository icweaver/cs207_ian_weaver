import my_proj.modules as m
import numpy as np
import pytest


def test_m__init__result():
    z = m.Complex(3, 4)
    assert z.r == 3
    assert z.i == 4
    assert z.mag == 5
    assert round(z.ang, 3) == 0.927

def test_m__init__types():
    with pytest.raises(TypeError):
        z = m.Complex()
    with pytest.raises(TypeError):
        z = m.Complex('')
    with pytest.raises(TypeError):
        z = m.Complex('a')
    with pytest.raises(TypeError):
        z = m.Complex(1, '')
    with pytest.raises(TypeError):
        z = m.Complex(1, 'a')
    with pytest.raises(TypeError):
        z = m.Complex('', 1)
    with pytest.raises(TypeError):
        z = m.Complex('a', 1)

def test_m_conj_result():
    z = m.Complex(1, 2)
    assert repr(z.conj()) == '1 - 2i'

def test_m_conj_types():
    z = m.Complex(1, 2)
    with pytest.raises(TypeError):
        z_conj = z.conj('a')

def test_m__add__result():
    z1 = m.Complex(1, 2)
    z2 = m.Complex(3, 4)
    assert repr(z2 - z1) == '2 + 2i'
    assert repr(8 -  z1) == '7 - 2i'

def test_m__add__types():
    with pytest.raises(TypeError):
        m.Complex(1, 2) + 'a' 
