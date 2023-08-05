from distutils.core import setup
setup(
  name = 'B3score',
  packages = ['B3score'], # this must be the same as the name above
  version = '0.1',
  description = 'BCUBED extrinsic clustering metric',
  author = 'Matthew Wiesner',
  author_email = 'wiesner@jhu.edu',
  url = 'https://github.com/m-wiesner/BCUBED',
  install_requires = ["numpy"],
  download_url = 'https://github.com/m-wiesner/BCUBED/tarball/0.1', # I'll explain this in a second
  keywords = ['clustering', 'bcubed', 'evaluation'], # arbitrary keywords
  classifiers = []
)
