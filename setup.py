from setuptools import setup, find_packages

exec(open("./dinogame/version.py").read())

with open('README.md') as f:
    _LONG_DESCRIPTION = f.read()

setup(
    name='dino-game',
    packages=find_packages(),
    version=__version__,
    license='gpl-3.0',
    description='A Python reimplementation of the famous dino game, thought for autonomous control',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Roberto Bochet',
    author_email='robertobochet@gmail.com',
    url='https://github.com/RobertoBochet/dino-game',
    keywords=['game', 'gym', 'dino', 'pygame'],
    install_requires=[
        'pygame>=2.0.0.dev6'
    ],
    package_data={'dinogame': ['assets/*.png']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)
