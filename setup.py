try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

setup(
    name='fv3grib2nc4',
    version='1.0',
    author='Barry D. Baker',
    maintainer='Barry Baker',
    packages=find_packages(),
    scripts=['fv3grib2nc4.py'],
    license='GPL',
    long_description=open('README.md').read(),
)
