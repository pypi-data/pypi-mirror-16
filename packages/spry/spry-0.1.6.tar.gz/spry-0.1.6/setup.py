from distutils.core import setup
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(
  name = 'spry',
  version = '0.1.6',
  description = 'Spry is a social media collector toolsuite',
  author = 'James Campbell',
  author_email = 'james@jamescampbell.us',
  url = 'https://github.com/jamesacampbell/spry', # use the URL to the github repo
  download_url = 'https://github.com/jamesacampbell/spry/tarball/0.1.6',

  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',],
      packages=["spry", "spry.modules"],
    package_data={'spry': ['sociallist/sociallist.txt']},
  install_requires = ['requests>=1.0'],

    entry_points={
        'console_scripts': [
            'spry=spry.spry:main',
        ],
    },

)
