import setuptools

setuptools.setup(
    name='eapp-python-domain',
    version='0.2.0',
    author='Amit Khetan',
    author_email='amit.khetan.70@50gramx.io',
    description='ethos applications entities and service contracts for python domain',
    packages=['eapp-python-domain'],
    install_requires=['protobuf', 'grpcio', 'grpcio-tools'],
)