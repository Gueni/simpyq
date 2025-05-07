from setuptools import setup, find_packages

setup(
    name='simpyq',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'simpyq=simpyq.cli:main',
        ],
    },
    install_requires=[
        'pyfiglet',
        # Add other dependencies like numpy, matplotlib, scikit-learn, etc.
    ],
    author='Mohamed Gueni',
    description='Natural Language Signal Query Tool for Simulation Data',
)
