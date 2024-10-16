from setuptools import setup, find_packages

setup(
    name='usefulgen',
    version='1.0.2',
    packages=find_packages(),
    description='A Python script containing some must-have generators',
    install_requires=['typing'],
    author='M4elstr0m',
    long_description='A Python module containing some must-have generators\nFor more details, don\'t hesitate to go on https://github.com/M4elstr0m/UsefulGenPy',
    url='https://github.com/M4elstr0m/UsefulGenPy',
    download_url='https://pypi.org/project/usefulgen/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose a license
    ],
)