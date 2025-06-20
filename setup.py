from setuptools import setup, find_packages

setup(
    name='dataset_generator',
    version='0.1.0',
    description='Modular synthetic data generator for NLP, vision, and tabular domains',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'flask',
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'dataset-generator=main:main',
            'dataset-generator-cli=cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['config/*.json'],
    },
    python_requires='>=3.7',
)
