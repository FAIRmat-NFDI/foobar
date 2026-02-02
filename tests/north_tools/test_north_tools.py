def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from foobar.north_tools.my_north_tool import (
        north_tool,
    )

    assert (
        north_tool.id_url_safe == 'foobar_my_north_tool'
        or north_tool.id == 'nomad-north-foobar'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
