from setuptools import setup
setup(
  name = 'apt-history',
  packages = ['apt_history'],
  version = '0.2.18',
  description = 'apt history script',
  author = 'Antti Leppa',
  author_email = 'antti.leppa@metatavu.fi',
  url = 'https://github.com/Metatavu/apt-history',
  download_url = 'https://github.com/Metatavu/apt-history/tarball/0.2.18', 
  keywords = ['apt'],
  classifiers = [],
  entry_points={
    'console_scripts': [
      'apt-history=apt_history:main',
    ],
  },
)