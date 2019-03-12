from timeconv import mm_to_hhmm
from timeconv import hhmm_to_mm


def test_mm_to_hhmm():
    
    assert mm_to_hhmm('83') == '1:23'
    assert mm_to_hhmm('180') == '3:00'
    assert mm_to_hhmm('181') == '3:01'
    assert mm_to_hhmm('179') == '2:59'
    assert mm_to_hhmm('5') == '0:05'
    assert mm_to_hhmm('0') == '0:00'

def test_hhmm_to_mm():

    assert hhmm_to_mm('1:13') == '73'
    assert hhmm_to_mm('0:13') == '13'
    assert hhmm_to_mm('0:0') == '0'
    assert hhmm_to_mm('10:00') == '600'
    assert hhmm_to_mm('10:01') == '601'
    assert hhmm_to_mm('09:59') == '599'