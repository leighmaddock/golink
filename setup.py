from setuptools import setup, find_packages

setup(
    name='golinks',
    version='0.0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pymongo'
    ],
)
