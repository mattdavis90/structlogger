StructLogger |Version| |Docs|
=============================

|Compatibility| |Implementations| |Format| |Code_Style|

Uses structlog to create two loggers, a stdout logger with key-value args and optional colour, and a 
file logger in JSON format with log-rotation.


Documentation
-------------
StructLogger's documentation can be found at `https://structlogger.readthedocs.io <https://structlogger.readthedocs.io>`_


Installing StructLogger
-----------------------
StructLogger can be installed from Pypi using pip::

    pip install structlogger


Example
-------

StructLogger defines a set of standard parameters that should get you going quickly and easily. Settings are retrofitted to 
the standard logging module to ensure any of your dependencies will adhere to the same logging format.

.. code :: python

   import structlog
   from structlogger import configure_logger, __version__

   configure_logger()

   log = structlog.getLogger()

   log.info('Welcome to structlogger', version=__version__)

.. |Version| image:: https://img.shields.io/pypi/v/structlogger.svg
   :target: https://pypi.python.org/pypi/structlogger
.. |Docs| image:: https://readthedocs.org/projects/structlogger/badge/?version=latest
   :target: https://structlogger.readthedocs.io
.. |Compatibility| image:: https://img.shields.io/pypi/pyversions/structlogger.svg
   :target: https://pypi.python.org/pypi/structlogger
.. |Implementations| image:: https://img.shields.io/pypi/implementation/structlogger.svg
   :target: https://pypi.python.org/pypi/structlogger
.. |Format| image:: https://img.shields.io/pypi/format/structlogger.svg
   :target: https://pypi.python.org/pypi/structlogger
.. |Code_Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
