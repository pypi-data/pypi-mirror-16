from setuptools import setup

setup(
    name='DBcm',
    version='1.6.1',
    description='The Head First Python 2e Database Context Manager',
    author='Paul Barry',
    author_email='paul.james.barry@gmail.com',
    url='http://www.headfirstlabs.com',
    py_modules=['DBcm'],
    dependency_links=['http://dev.mysql.com/downloads/connector/python/'],
    licence='MIT',
    install_requires=['mysql-connector-python'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    
)
