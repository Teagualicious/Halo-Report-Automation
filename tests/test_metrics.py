import math

import pytest

from halo.metrics import (
    SearchCell,
    additive_share_of_search_did,
    brand_share_of_search,
    ratio_of_ratios_lift,
)


def test_ratio_of_ratios_worked_example() -> None:
    lift = ratio_of_ratios_lift(
        SearchCell(50, 100),
        SearchCell(70, 100),
        SearchCell(50, 100),
        SearchCell(55, 100),
    )
    assert math.isclose(lift, 0.2727272727, rel_tol=1e-9)


def test_additive_share_of_search_did() -> None:
    did = additive_share_of_search_did(
        SearchCell(50, 100),
        SearchCell(70, 100),
        SearchCell(50, 100),
        SearchCell(55, 100),
    )
    expected = (70 / 170 - 50 / 150) - (55 / 155 - 50 / 150)
    assert math.isclose(did, expected, rel_tol=1e-12)


def test_brand_share_rejects_all_zero() -> None:
    with pytest.raises(ValueError):
        brand_share_of_search(0, 0)


def test_ratio_of_ratios_rejects_zero_brand() -> None:
    with pytest.raises(ValueError):
        ratio_of_ratios_lift(
            SearchCell(0, 100),
            SearchCell(1, 100),
            SearchCell(1, 100),
            SearchCell(1, 100),
        )
