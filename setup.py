from setuptools import setup, find_packages

setup(
    name='groundhog',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/arabinelli/Groundhog',
    license='MIT',
    author='Andrea Rabinelli',
    author_email='andrea.rabinelli@gmail.com',
    description=" A simple decorator to get notified when your pre-alpha code fails",
    install_requires=[
        'slackclient==2.1.0',
        'slackeventsapi>=2.1.0',
        'certifi'
    ]
)