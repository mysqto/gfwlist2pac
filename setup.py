from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="gfwlist2pac",
    version="1.1.4",
    license='MIT',
    description="convert gfwlist2pac to pac, originaly by clowwindy, maintained by mysqto now",
    author='originally by @clowwindy, currently maintained by @mysqto',
    author_email='my@mysq.to',
    url='https://github.com/mysqto/gfwlist2pac',
    packages=['gfwlist2pac', 'gfwlist2pac.resources'],
    package_data={
        'gfwlist2pac': ['README.rst', 'LICENSE', 'resources/*']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    gfwlist2pac = gfwlist2pac.main:main
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    long_description=long_description,
)
