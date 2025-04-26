from setuptools import setup, find_packages

setup(name = 'Montecarlo_Simulator',
      version = '1.1',
      packages=find_packages(),
      description = 'Python Package for Montecarlo Simulator',
      url = 'https://github.com/Franc6s/montecarlo_simulator_pgm2qm',
      author = 'Francis Mangala',
      author_email = 'pgm2qm@virginia.edu',
      license = 'MIT',
      install_requires = ['numpy', 'pandas'])