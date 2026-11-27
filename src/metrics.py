"""Forecasting evaluation metrics (MAE, RMSE, MAPE)."""

from __future__ import annotations

import math
from typing import Sequence


def _validate_inputs(y_true: Sequence[float], y_pred: Sequence[float]) -> tuple[list[float], list[float]]:
    actual = [float(v) for v in y_true]
    predicted = [float(v) for v in y_pred]
    if not actual:
        raise ValueError("y_true and y_pred must not be empty.")
    if len(actual) != len(predicted):
        raise ValueError(f"Length mismatch: len(y_true)={len(actual)} vs len(y_pred)={len(predicted)}.")
    return actual, predicted


def mae(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    """Compute Mean Absolute Error."""
    actual, predicted = _validate_inputs(y_true, y_pred)
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


def rmse(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    """Compute Root Mean Squared Error."""
    actual, predicted = _validate_inputs(y_true, y_pred)
    return math.sqrt(sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual))


def mape(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    """Compute Mean Absolute Percentage Error (%) ignoring zero actuals."""
    actual, predicted = _validate_inputs(y_true, y_pred)
    pairs = [(a, p) for a, p in zip(actual, predicted) if a != 0.0]
    if not pairs:
        raise ValueError("MAPE is undefined when all actual values are zero.")
    return (sum(abs((a - p) / a) for a, p in pairs) / len(pairs)) * 100.0
