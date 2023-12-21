import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).parent.parent))

import SPFinance.scraper as scraper


def test_smt():
    assert 1 == 1
