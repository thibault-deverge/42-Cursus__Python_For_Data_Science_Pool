# setup.py
from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='tdeverge',
    author_email='tdeverge@42.fr',
    description='A simple package to fetch random facts.',
    url='https://github.com/tdeverge/blablabla',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
