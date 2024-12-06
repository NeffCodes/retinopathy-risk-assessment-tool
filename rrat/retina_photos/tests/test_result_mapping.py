import pytest
from retina_photos.utils import get_prognosis_choice
from retina_photos.choices import PrognosisChoices
def test_get_prognosis_choice_correct():
    assert get_prognosis_choice(0) == PrognosisChoices.NORMAL
    assert get_prognosis_choice(1) == PrognosisChoices.MILD
    assert get_prognosis_choice(2) == PrognosisChoices.MODERATE
    assert get_prognosis_choice(3) == PrognosisChoices.SEVERE
    assert get_prognosis_choice(4) == PrognosisChoices.PROLIFERATIVE

def test_get_prognosis_choice_incorrect():
    assert get_prognosis_choice(-1) is None
    assert get_prognosis_choice(5) is None
    assert get_prognosis_choice('invalid') is None
    assert get_prognosis_choice(None) is None
    assert get_prognosis_choice('0') is None
    assert get_prognosis_choice(0.5) is None
