from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/ronniyjoseph/WorkshopExample',
      author='Ronniy Joseph',
      author_email='ronniy.joseph@postgrad.curtin.edu.au',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
