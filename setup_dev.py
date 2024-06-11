import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# NOTE: DO NOT EDIT ANYTHING TILL LINE NO 10
setup(
    name='ethosdev',
    version='0.0.1',
    author='Paras Verma',
    author_email='peivee@50gramx.io',
    description='ethos applications entities and service contracts for python dev domain',
    packages=find_packages(where='src/eapp_python_domain'),
    package_dir={'': 'src/eapp_python_domain'},
    install_requires=['protobuf>=3.14.0', 'grpcio>=1.34.0', 'grpcio-tools>=1.34.0'],
)

# find eapp_python_domain/ethos/elint -type d -exec touch {}/__init__.py \;
