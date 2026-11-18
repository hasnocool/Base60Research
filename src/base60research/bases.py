# src/base60research/bases.py
"""Exact integer and rational representation helpers."""
from __future__ import annotations
from fractions import Fraction
from math import gcd

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode_integer(value: int, base: int = 60) -> str:
    if not 2 <= base <= len(DIGITS):
        raise ValueError(f"base must be between 2 and {len(DIGITS)}")
    if value == 0:
        return "0"
    sign, n = ("-" if value < 0 else ""), abs(value)
    out = []
    while n:
        n, rem = divmod(n, base)
        out.append(DIGITS[rem])
    return sign + "".join(reversed(out))

def decode_integer(text: str, base: int = 60) -> int:
    if not 2 <= base <= len(DIGITS):
        raise ValueError("unsupported base")
    raw = text.strip()
    if not raw:
        raise ValueError("empty numeral")
    sign = -1 if raw.startswith("-") else 1
    raw = raw[1:] if raw[:1] in "+-" else raw
    value = 0
    for char in raw:
        digit = DIGITS.find(char)
        if digit < 0 or digit >= base:
            raise ValueError(f"digit {char!r} is invalid in base {base}")
        value = value * base + digit
    return sign * value

def fraction_terminates(value: Fraction, base: int = 60) -> bool:
    """True iff the reduced denominator divides some power of base."""
    denominator = value.denominator
    while denominator > 1:
        common = gcd(denominator, base)
        if common == 1:
            return False
        denominator //= common
    return True

def sexagesimal(value: float | Fraction, places: int = 4) -> str:
    """Format a real number using base-60 positional fractional digits."""
    if places < 0:
        raise ValueError("places must be non-negative")
    number = float(value)
    sign = "-" if number < 0 else ""
    number = abs(number)
    whole = int(number)
    remainder = number - whole
    parts = [str(whole)]
    for _ in range(places):
        remainder *= 60
        digit = int(remainder)
        parts.append(str(digit))
        remainder -= digit
    return sign + ";".join(parts)

def degrees_to_sexagesimal(degrees: float, places: int = 3) -> str:
    return sexagesimal(degrees, places)

def compare_fraction_finiteness(value: Fraction, bases=(10, 12, 24, 30, 60, 360)) -> dict[str, bool]:
    return {str(base): fraction_terminates(value, base) for base in bases}
