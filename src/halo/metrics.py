"""Transparent audit calculations for Halo analysis.

These functions implement the simple executive calculations. They do not
replace the production multi-period model, uncertainty estimation, or QA.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SearchCell:
    """Brand and category relative-search indices for one group-period cell."""

    brand: float
    category: float

    def validate(self) -> None:
        if self.brand < 0:
            raise ValueError("brand must be nonnegative")
        if self.category <= 0:
            raise ValueError("category must be greater than zero")


def brand_share_of_search(brand: float, category: float) -> float:
    """Return brand / (brand + category) for nonnegative relative indices."""

    if brand < 0 or category < 0:
        raise ValueError("brand and category must be nonnegative")
    denominator = brand + category
    if denominator <= 0:
        raise ValueError("brand + category must be greater than zero")
    return brand / denominator


def ratio_of_ratios_lift(
    treated_pre: SearchCell,
    treated_post: SearchCell,
    control_pre: SearchCell,
    control_post: SearchCell,
) -> float:
    """Return multiplicative difference-in-differences lift as a decimal.

    Formula:
      ((treated_post brand/category) / (treated_pre brand/category))
      ---------------------------------------------------------------- - 1
      ((control_post brand/category) / (control_pre brand/category))
    """

    for cell in (treated_pre, treated_post, control_pre, control_post):
        cell.validate()
        if cell.brand <= 0:
            raise ValueError("brand must be greater than zero for ratio-of-ratios")

    treated_change = (treated_post.brand / treated_post.category) / (
        treated_pre.brand / treated_pre.category
    )
    control_change = (control_post.brand / control_post.category) / (
        control_pre.brand / control_pre.category
    )
    return treated_change / control_change - 1.0


def additive_share_of_search_did(
    treated_pre: SearchCell,
    treated_post: SearchCell,
    control_pre: SearchCell,
    control_post: SearchCell,
) -> float:
    """Return additive DiD in brand-share-of-search percentage-point units."""

    treated_delta = brand_share_of_search(
        treated_post.brand, treated_post.category
    ) - brand_share_of_search(treated_pre.brand, treated_pre.category)
    control_delta = brand_share_of_search(
        control_post.brand, control_post.category
    ) - brand_share_of_search(control_pre.brand, control_pre.category)
    return treated_delta - control_delta
