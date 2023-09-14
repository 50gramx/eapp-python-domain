import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# NOTE: DO NOT EDIT ANYTHING TILL LINE NO 10
setup(
    name='eapp_python_domain',
    version='0.2.22',
    author='Amit Khetan',
    author_email='amit.khetan.70@50gramx.io',
    description='ethos applications entities and service contracts for python domain',
    package_dir = {"": "src"},
    packages=['eapp_python_domain'],
    install_requires=['protobuf', 'grpcio', 'grpcio-tools'],
    include_package_data=True
)