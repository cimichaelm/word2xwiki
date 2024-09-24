from setuptools import setup, find_packages

setup(
    name='word2xwiki',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'word2xwiki=word2xwiki:main',
        ],
    },
)
