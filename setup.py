from setuptools import setup, find_packages


setup(
    name='PyHostr',
    version='0.2',
    license='MIT',
    author="Sami Hindi",
    author_email='sami@samihindi.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/FujiwaraChoki/PyHost',
    keywords='PyHostr',
    install_requires=[
        'http.server',
    ],
)
