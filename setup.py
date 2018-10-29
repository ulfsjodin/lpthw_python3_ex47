#setup file for exercise 46

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My project',
        'author': 'Ulf Sjödin',
        'url': 'Github',
        'download_url': 'www.xxx',
        'author_email': 'sjodin.ulf@gmail.com',
        'version': '0.1',
        'install_requires': 'pytest',
        'packages': ['NAME'],
        'scripts': [],
        'name': 'project_name'
        
        }

setup(**config)
