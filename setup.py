from setuptools import setup, find_packages

setup(
    name='dumbrute',
    version='0.1.0',
    packages=find_packages(include=["dumbrute"]),
    install_requires=["requests"],
    entry_points={
        'console_scripts': ['dumbrute=dumbrute.cli:entrypoint']
    }
)
