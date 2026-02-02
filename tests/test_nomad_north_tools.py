"""Tests for the NOMAD NORTH tool."""

import pytest

try:
    import nomad  # noqa: F401
except ImportError:
    pytest.skip(
        "Skipping NOMAD NORTH tool tests because nomad-lab is not installed",
        allow_module_level=True,
    )


def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from pynxtools_foo.nomad.north_tools.foo import (
        north_tool,
    )

    assert (
        north_tool.id_url_safe == 'pynxtools_foo_foo'
        or north_tool.id == 'nomad-north-foo'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
