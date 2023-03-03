from setuptools import setup, find_packages

setup(
    name='cli_for_fastapi',
    version='0.1.0',
    author='Group 10',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'src=src.cli:app',
        ],
    },
    install_requires=[
        "numpy",
        "pandas",
        "typer",
        "requests",
        "click",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)