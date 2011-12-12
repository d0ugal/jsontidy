import os
try:
    from setuptools import setup
    kw = {'entry_points':
          """[console_scripts]\njsontidy= jsontidy:main\n""",
          'zip_safe': False}
except ImportError:
    from distutils.core import setup
    kw = {'scripts': ['jsontidy']}

here = os.path.dirname(os.path.abspath(__file__))

setup(name='jsontidy',
      version="0.1.0",
      description="JSON Prettify Utility",
      long_description="""
A simple command line utility to pretty print JSON output from other command
line tools with pipes. For example "my_command | jsontidy".
      """,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
      keywords='json',
      author='Dougal Matthews',
      author_email='dougal85@gmail.com',
      maintainer='Dougal Matthews',
      maintainer_email='dougal85@gmail.com',
      url='https://github.com/d0ugal/rawr',
      license='MIT',
      py_modules=['jsontidy'],
      **kw
      )
