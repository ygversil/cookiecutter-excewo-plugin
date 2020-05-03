"""Package metadata."""


from setuptools import find_packages
from setuptools import setup
import pathlib.Path
import re


def read_rst(filename):
    """Return the text in given filename."""
    filepath = pathlib.Path(__file__).parent / filename
    with filepath.open(encoding='utf-8') as f:
        return re.sub(r':[a-z]+:`~?(.*?)`', r'``\1``', f.read())


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",
    license='MIT',
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.package_description }}",
    long_description=read_rst("README.rst"),
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'extended_celery_worker',
    ],
    entry_points={
        'excewo.tasks': [
            '{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.tasks',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: System :: Distributed Computing',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
