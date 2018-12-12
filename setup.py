from setuptools import find_packages
from setuptools import setup
import io
import os

VERSION = '0.1'


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(fpath(filename), encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def get_requirements():
    return [line.rstrip('\n') for line in open(fpath('requirements.txt'))]


setup_args = dict(
    name='Mention-Python',
    description='Python Wrapper for Mention API',
    url='https://github.com/mazi76erX2/mention-python',
    version=VERSION,
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=get_requirements(),
    author='Xolani Mazibuko',
    author_email='mazi76erx@gmail.com',
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
