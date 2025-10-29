#!/usr/bin/env python3
"""
Test package metadata and imports
"""

import pytest

from triss25 import (
    __maintainer__,
    __project_name__,
    __version__,
    __license__,
)


@pytest.mark.unit
def test_package_metadata():
    """Test that package metadata is accessible."""

    assert __maintainer__ == "jonzeolla"
    assert __project_name__ == "triss25"
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert __license__ == "MIT"
