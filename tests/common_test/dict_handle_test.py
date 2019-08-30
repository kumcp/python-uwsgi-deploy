import pytest
from source.base.common.dict_handle import *


def test_compute_list_dict():
    """Compute a list of dictionary. This is the simple case of
    computing sum of all parameters exist in the dict. All dicts
    has the same list of keys
    """

    list_dict = [
        {"item": 3},
        {"item": 4}
    ]

    def summary_func(prev, current):

        for key in current:
            if prev.get(key) is not None:
                prev[key] = prev[key] + current[key]
            else:
                prev[key] = current[key]

        return prev

    result = compute_list_dict(summary_func, *list_dict)

    assert result["item"] == 7


def test_compute_list_different_dict():
    """Compute a list of dictionary. This is the case of
    computing sum of all parameters in the dict with different
    keys list
    """

    list_dict = [
        {"item": 3},
        {"item": 4, "price": 30}
    ]

    def summary_func(prev, current):

        for key in current:
            if prev.get(key) is not None:
                prev[key] = prev[key] + current[key]
            else:
                prev[key] = current[key]

        return prev

    result = compute_list_dict(summary_func, *list_dict)

    assert result["item"] == 7
    assert result["price"] == 30


def test_summary_list_dict():

    list_dict = [
        {"item": 3},
        {"item": 4},
        {"item": 5},
    ]

    result = summary_list_dict(*list_dict)

    assert result["item"] == 12


@pytest.mark.skip(reason="Not implemented yet")
def test_map_list_dict():
    assert False
