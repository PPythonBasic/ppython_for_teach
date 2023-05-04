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
    # Explicitly specify the packages to include
    packages=["ppy"],
    # Exclude the 'assets' directory from the package data
    package_data={"ppy": ["*"], "": ["LICENSE"]},
    exclude_package_data={"ppy": ["assets/*"]},
)
setuptools.setup(**setup_args)
