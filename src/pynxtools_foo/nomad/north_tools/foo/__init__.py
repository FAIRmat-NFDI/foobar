from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin pynxtools-foo.',
    image='ghcr.io/RubelMozumder/pynxtools-foo/jupyter:latest',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin pynxtools-foo.',
    external_mounts=[],
    file_extensions=['ipynb', 'nxs', 'h5', 'hdf5'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'fairmat@physik.hu-berlin.de', 'name': ''}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='foo',
)

north_tool = NorthToolEntryPoint(
    id_url_safe='pynxtools_foo_foo', north_tool=tool
)
