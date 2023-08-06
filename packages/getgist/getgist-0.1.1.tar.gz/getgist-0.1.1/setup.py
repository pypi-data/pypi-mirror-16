from setuptools import setup

REPO_URL = 'http://github.com/cuducos/getgist'


setup(author='Eduardo Cuducos',
      author_email='cuducos@gmail.com',
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Intended Audience :: Developers',
                   'Topic :: Utilities',
                   'License :: OSI Approved :: MIT License'],
      description='CLI to update local and remote files from GitHub gists',
      entry_points={'console_scripts': ['getgist=getgist.__main__:run_getgist',
                                        'getmy=getgist.__main__:run_getmy',
                                        'putgist=getgist.__main__:run_putgist',
                                        'putmy=getgist.__main__:run_putmy']},
      include_package_data=True,
      install_requires=['click>=5.1', 'requests>=2.10.0'],
      keywords='gist, command-line, github, dotfiles',
      license='MIT',
      long_description='Check `GetGist at GitHub <{}>`_.'.format(REPO_URL),
      name='getgist',
      packages=['getgist'],
      setup_requires=['tox-setuptools'],
      url=REPO_URL,
      version='0.1.1',
      zip_safe=False)
