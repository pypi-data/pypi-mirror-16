from distutils.core import setup
VERSION = '0.3.2'
setup(
  name = 'jkspy',
  install_requires = ['pytz', 'Pillow', 'numpy'],
  packages = ['jkspy',
              'jkspy.modules',
              'jkspy.apps',
              'jkspy.django',],
  package_data = {'jkspy':['scripts/*']},
  scripts = ['jkspy/scripts/checksum', 'jkspy/scripts/jkspy'],
#   entry_points = {
#                   'console_scripts': [
#                                       'checksum = jkspy.scripts.checksum',
#                                       ],
#                   },
#   data_files = [('', 'LICENSE.txt')],
  version = VERSION,
  description = 'Python utilities for doing computer stuff',
  author = 'Kumseok Jung',
  author_email = 'jungkumseok@gmail.com',
  license = 'LICENSE.txt',
  url = 'https://github.com/jungkumseok/jkspy',
  download_url = 'https://github.com/jungkumseok/jkspy/archive/'+VERSION+'.tar.gz',
  keywords = ['testing', 'utility'], 
  classifiers = [],
)
