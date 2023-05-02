import setuptools

from ppy import __app_name__, __version__

setup_args = dict(
    name=__version__,
    version="0.1.0",
    description="PPython Basic for Teach",
    author="wk18k",
    entry_points="""
    [console_scripts]
    ppy=ppy.cli:main
    """,
)
setuptools.setup(**setup_args)
