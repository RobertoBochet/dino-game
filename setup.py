from distutils.core import setup

setup(
    name='dino-game',
    packages=['dinogame'],
    version='0.1',
    license='gpl-3.0',
    description='A Python reimplementation of the famous dino game, thought for autonomous control',
    author='Roberto Bochet',
    author_email='robertobochet@gmail.com',
    url='https://github.com/RobertoBochet/dino-game',
    keywords=['game', 'gym', 'dino', 'pygame'],
    install_requires=[
        'pygame>=2.0.0.dev6',
        'numpy'
    ],
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
