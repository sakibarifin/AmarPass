
import pytest
from project import chars, bn_words, save


def test_chars():
    assert len(chars(3)) == 3
    assert len(chars(6)) == 6
    # Maybe I should restrict the number of chars in a future update
    assert len(chars(10)) == 10


def test_bn_words():
    assert len(bn_words(3)) == 3
    assert len(bn_words(6)) == 6
    # The number of words param should be restricted to 12 or 24 words max in a future update
    assert len(bn_words(12)) == 12


def test_save():
    with pytest.raises(ValueError):
        save(None)
