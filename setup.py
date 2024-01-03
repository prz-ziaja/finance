from setuptools import setup, find_packages

setup(name='SPFinance',
    version='0.1',
    description='Szymon&Przemek Finance library.',
    packages=find_packages(where='src', exclude=['tests', 'sql']),
    package_dir={'': 'src'},
    url="https://github.com/prz-ziaja/finance",
    author="Szymon Duda, Przemek Ziaja",
    author_email="author@example.com",
    extras_require={
        'scraper': [
            # List dependencies for the "example" extra feature here, eg: yfinance, pandas....
            'extra_dependency1',
            'extra_dependency2',
        ],
        'consumer': [
            # List dependencies for the "example" extra feature here, eg: psql.... -> the main goal is to separate requirements so scraper do not install pyspark
            'extra_dependency1',
            'extra_dependency2',
        ],
    },
)
