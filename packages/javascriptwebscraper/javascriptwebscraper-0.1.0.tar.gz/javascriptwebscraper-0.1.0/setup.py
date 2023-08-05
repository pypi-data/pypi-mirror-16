import os
from setuptools import find_packages, setup


# directory = os.path.abspath(os.path.dirname(__file__))
"""
with open(os.path.join(directory, 'README.rst')) as f:
    long_description = f.read()
"""

setup(
    name="javascriptwebscraper",
    version='0.1.0',
    description='javascript webscaper for youtube for Vexbot',
    # long_description=long_description,
    url='https://github.com/benhoff/javascriptwebscraper',
    license='GPL3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Utilities',
        'Operating System :: OS Independent'],
    keywords='youtube javascript webscraper',
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    entry_points={'vexbot.adapters': ['javascriptwebscraper = javascriptwebscraper.__main__']},

    packages= find_packages(), # exclude=['docs', 'tests']
    install_requires=[
        'pyzmq',
        'vexbot',
        'vexmessage',
        'selenium',
        ],

    extras_require={
        'dev': ['flake8']
        },
)
