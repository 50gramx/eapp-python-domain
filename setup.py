import setuptools

setuptools.setup(
    name='eapp-python-domain',
    version='0.2.10',
    author='Amit Khetan',
    author_email='amit.khetan.70@50gramx.io',
    description='ethos applications entities and service contracts for python domain',
    packages=setuptools.find_packages('eapp-python-domain.eapp-python-domain'),
    install_requires=['protobuf', 'grpcio', 'grpcio-tools'],
    include_package_data=True
)
