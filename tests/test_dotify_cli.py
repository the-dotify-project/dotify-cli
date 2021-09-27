"""Tests concerning the `dotify_cli` module."""

from dotify_cli.dotify_cli import factorial


def test_dotify_cli():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
