#!/usr/bin/env python3
"""Multiplier Annotated Function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by multiplier
    """
    def multiply(num: float) -> float:
        """Multiplies a float by a multiplier"""
        return multiplier * num

    return multiply
