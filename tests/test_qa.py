from halo.qa import missing_required_fields, validate_nonnegative_row


def test_missing_required_fields() -> None:
    missing = missing_required_fields({"client_alias", "campaign_id"})
    assert "week_start" in missing
    assert "brand_rsv" in missing


def test_nonnegative_row_validation() -> None:
    errors = validate_nonnegative_row({"brand_rsv": 10, "category_rsv": 20, "impressions": -1})
    assert errors == ["impressions must be nonnegative"]
