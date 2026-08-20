"""Small reusable QA checks for governed Halo input tables."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


REQUIRED_GEO_WEEK_FIELDS = {
    "client_alias",
    "campaign_id",
    "analysis_geo_id",
    "week_start",
    "brand_rsv",
    "category_rsv",
    "impressions",
}


def missing_required_fields(fields: Iterable[str]) -> set[str]:
    """Return required geo-week fields missing from an input schema."""

    return REQUIRED_GEO_WEEK_FIELDS.difference(set(fields))


def validate_nonnegative_row(row: Mapping[str, Any]) -> list[str]:
    """Return validation errors for numeric fields that cannot be negative."""

    errors: list[str] = []
    for field in ("brand_rsv", "category_rsv", "impressions", "reach", "spend"):
        value = row.get(field)
        if value is not None and value < 0:
            errors.append(f"{field} must be nonnegative")
    return errors
