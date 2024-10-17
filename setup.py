from setuptools import setup, find_packages

setup(
    name='usefulgen',
    version='1.0.3.1',
    packages=find_packages(),
    description='Python Module dedicated to time-saving generators, made by M4elstr0m',
    install_requires=['typing'],
    author='M4elstr0m',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/M4elstr0m/UsefulGenPy',
    download_url='https://pypi.org/project/usefulgen/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
    ],
)

#python setup.py sdist bdist_wheel
#twine upload dist/*