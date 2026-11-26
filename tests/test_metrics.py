"""Unit tests for forecasting evaluation metrics."""

import math
import pytest
from src.metrics import mae, mape, rmse


def test_metrics_exact_match() -> None:
    y = [100.0, 200.0, 300.0]
    assert mae(y, y) == 0.0
    assert rmse(y, y) == 0.0
    assert mape(y, y) == 0.0


def test_metrics_known_values() -> None:
    y_true = [100.0, 200.0]
    y_pred = [110.0, 180.0]
    assert math.isclose(mae(y_true, y_pred), 15.0)
    assert math.isclose(rmse(y_true, y_pred), math.sqrt((100.0 + 400.0) / 2.0))
    assert math.isclose(mape(y_true, y_pred), 10.0)


def test_mape_skips_zero_actuals() -> None:
    assert math.isclose(mape([0.0, 100.0], [10.0, 90.0]), 10.0)


def test_metrics_validation_errors() -> None:
    with pytest.raises(ValueError):
        mae([], [])
    with pytest.raises(ValueError):
        rmse([1.0, 2.0], [1.0])
    with pytest.raises(ValueError):
        mape([0.0, 0.0], [1.0, 2.0])
