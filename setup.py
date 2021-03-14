import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="todolist",
    version="1.0.0",
    url="",
    license="BSD",
    maintainer="Gideon Mandu",
    maintainer_email="gideonmandu@gmail.com",
    description="The basic todo list app built in Flask.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "pymongo, bson"],
    extras_require={"test": ["pytest", "coverage"]},
)