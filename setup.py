from setuptools import setup, find_packages

setup(
    name='DemoMastersOfCode2015',
    version='0.0.1',
    url='https://bla.com/',
    author='Felipe Blassioli',
    author_email='felipeblassioli@gmail.com.br',
    description='Meant to be run on tablets.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'flask-peewee>=0.6.6',
        'flask-classy>=0.6.8',
        'simplifycommerce-sdk-python',
        'Flask-Admin',
    ],
)
