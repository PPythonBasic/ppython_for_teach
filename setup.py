import setuptools

from ppy import __app_name__, __version__

setup_args = dict(
    name="ppy",
    version=__version__,
    description="PPython Basic for Teach",
    author="wk18k",
    entry_points="""
    [console_scripts]
    ppy=ppy.cli:main
    """,
)
setuptools.setup(**setup_args)
