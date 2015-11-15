#!/usr/bin/env python

from setuptools import setup
import os

# MUST ASSERT THAT python-dev is installed

setup(name='abce',
      version='0.4b',
      author='Davoud Taghawi-Nejad',
      author_email='Davoud@Taghawi-Nejad.de',
      description='Agent-Based Complete Economy modelling platform',
      url='https://github.com/DavoudTaghawiNejad/abce.git',
      package_dir={'abce': 'abce'},
      packages=['abce'],
      long_description=open('README.rst').read(),
      install_requires=['numpy', 'scipy', 'dataset', 'pandas', 'networkx'],
      include_package_data=True)

print('** **************************************************************************')
print('**                                                                         **')
print('** - To use ABCE download templates and examples from                      **')
print('**                                                                         **')
print('**    github.com/DavoudTaghawiNejad/abce                                   **')
print('**    or                                                                    **')
print('**    https://github.com/DavoudTaghawiNejad/abce/archive/master.zip        **')
print('**                                                                         **')
print('** - documentation http://davoudtaghawinejad.github.com/abce/              **')
print('**                                                                         **')
print('*****************************************************************************')
if os.name == 'posix':
    try:
        subprocess.call(["tar", "xf abce-0.3.tar.gz"])
    except:
        print('** Please unzip abce-0.3.tar.gz. There you will find examples, templates and documentation')
        print('** - documentation http://davoudtaghawinejad.github.com/abce/')
elif os.name == 'Darwin':
    try:
        subprocess.call(["tar", "xf abce-0.3.tar.gz"])
    except:
        print('** Please unzip abce-0.3.tar.gz. There you will find examples, templates and documentation')
        print('** - documentation http://davoudtaghawinejad.github.com/abce/')
else:
  print('** Please unzip abce-0.3.tar.gz. There you will find examples, templates and documentation')
  print('** - documentation http://davoudtaghawinejad.github.com/abce/')
