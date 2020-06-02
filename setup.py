try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='structlogger',
    version='0.1.4',
    description='Uses structlog to create two loggers, a stdout logger with key-value args and optional colour, and a file logger in JSON format with log-rotation.',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "homepage": "https://github.com/mattdavis90/structlogger",
        "repository": "https://github.com/mattdavis90/structlogger"
    },
    author='Matt Davis',
    author_email='mattdavis90@googlemail.com',
    license='MIT',
    packages=['structlogger'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'python-json-logger==0.*,>=0.1.9', 'structlog[dev]==20.*,>=20.1.0'
    ],
)
