from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'slackbot/VERSION')).read().strip()

install_requires = (
    'requests',
    'websocket-client',
    'slack-sdk',
) # yapf: disable

excludes = (
    '*test*',
    '*local_settings*',
) # yapf: disable

setup(name='slackbotng',
      version=__version__,
      license='MIT',
      description='A simple chat bot for Slack',
      author='Adrian Muraru',
      author_email='adi.muraru@gmail.com',
      url='http://github.com/amuraru/slackbot',
      platforms=['Any'],
      long_description=open("README.md", 'r').read(),
      long_description_content_type='text/markdown',
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6'])
