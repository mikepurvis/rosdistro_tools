from setuptools import setup


setup(
    name='rosdistro_tools',
    version='0.1',
    author='Mike Purvis',
    author_email='mpurvis@clearpathrobotics.com',
    packages=['rosdistro_tools'],
    url='',
    license='See LICENSE.txt',
    description='Tools for working with rosdistro repos.',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [ 'rosdistro = rosdistro_tools.commands.rosdistro:main' ]
    },
)
