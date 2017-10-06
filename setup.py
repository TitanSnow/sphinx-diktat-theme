from setuptools import setup


setup(
    name='diktat',
    version='0.1.dev2',
    description='A material designed sphinx theme for private use',
    long_description=open('README.rst').read(),
    author='TitanSnow',
    author_email='tttnns1024@gmail.com',
    url='https://github.com/TitanSnow/sphinx-diktat-theme',
    packages=['diktat'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'diktat = diktat',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
    ],
    install_requires=[
        'sphinx~=1.6.1',
    ]
)
