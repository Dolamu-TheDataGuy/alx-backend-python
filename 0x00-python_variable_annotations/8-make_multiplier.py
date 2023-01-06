#!/usr/bin/env python3
"""Multiplier Annotated Function"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that takes a float multiplier
    as an argument and returns a function that multiplies a float by a multiplier"""
    def multiply(num: float) -> float:
        """Multiplies a float by a multiplier"""
        return multiplier * num
    return multiply
