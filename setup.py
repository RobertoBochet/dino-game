from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dino-game',
    packages=['dinogame'],
    version='0.1a1',
    license='gpl-3.0',
    description='A Python reimplementation of the famous dino game, thought for autonomous control',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roberto Bochet',
    author_email='robertobochet@gmail.com',
    url='https://github.com/RobertoBochet/dino-game',
    keywords=['game', 'gym', 'dino', 'pygame'],
    install_requires=[
        'pygame>=2.0.0.dev6',
        'numpy'
    ],
    package_data={'dinogame': ['assets/*.png']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)
