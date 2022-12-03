from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='PyHostr',
    version='0.4',
    license='MIT',
    author="Sami Hindi",
    author_email='sami@samihindi.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/FujiwaraChoki/PyHost',
    keywords='PyHostr',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
