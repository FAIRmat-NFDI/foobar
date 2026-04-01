from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin foobar.',
    image='ghcr.io/fairmat-nfdi/foobar:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin foobar.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'john.doe@physik.hu-berlin.de', 'name': 'John Doe'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='tool',
)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='foobar-tool',
    north_tool=tool,
)
