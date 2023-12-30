from setuptools import setup, find_packages

setup(name='SPFinance',
      version='0.1',
      description='Szymon&Przemek Finance library.',
      packages=find_packages(where='src', exclude=['tests', 'sql']),
      package_dir={'': 'src'},
      url="https://github.com/pypa/sampleproject",
          author="Example Author",
    author_email="author@example.com",
)
