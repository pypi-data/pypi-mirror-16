from setuptools import setup, find_packages

import re
import os

version = '0.2.0'

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

try:
    import pypandoc
    read_md = lambda f: pypandoc.convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='PreTrainingChain',
      version=version,
      description='Scalable, configurable and Pre-training DNN using chainer',
      #long_description=read_md('README.rst'),
      keywords='chainer, newral network, machine leaning',
      author='Ryosuke Fukatani',
      author_email='nannyakannya@gmail.com',
      url='https://github.com/fukatani/PreTrainingChain',
      license="Apache License 2.0",
      packages=find_packages(),
      package_data={ 'PreTrainingChain' : ['testcode/*'], },
      #long_description=read_md('Readme.md'),
      #install_requires=["chainer", "sklearn"]
)

