def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from foobar.north_tools import north_entry_point

    expected_id = 'foobar-tool'
    assert (
        north_entry_point.id_url_safe == expected_id
        or north_entry_point.id == 'nomad-north-foobar'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
