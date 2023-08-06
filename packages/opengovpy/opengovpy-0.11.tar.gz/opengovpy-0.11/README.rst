Opengovpy
=========

opengovpy is a simple Python wrapper around `Moscow open data api <http://api.data.mos.ru>`_

It works as follows: you create a class instance of ``api``,
then call it with parameters::

    from opengovpy import api

    # You may specify your api key when instantiating this
    # like this using ``key`` argument: example = api(key='yourapikey')
    example = api()

    # To get dataset list (http://api.data.mos.ru/Docs#datasetsList):
    dataset_list = example()

    # To ged dataset passport (http://api.data.mos.ru/Docs#datasetPassport)
    dataset_passport = example(id=658)

    # To get dataset rows (http://api.data.mos.ru/Docs#datasetRows)
    dataset_rows = example(id=658, rows=True)

    # To count number of rows in a dataset ()
    dataset_rows = example(id=658, count=True)

    # To get geodata (http://api.data.mos.ru/Docs#datasetFeatures):
    dataset_features = example(id=1786, features=True)

    # It is also possible to specify coords to look up:
    dataset_features = example(id=1786, features=True,
                                  bbox=[37.49711036682129, 55.86543869723485, 37.5490379333496, 55.89110103788533])

    # You may specify OData parameters supported by api (http://api.data.mos.ru/Docs#OData)
    # like this:
    dataset = example(id=658, rows=True, top=3, orderby='Number')
    dataset = example(skip=10, inlinecount=True, top=5)

The returned value is always a python object (deserialized json, with accordance to `this table <https://docs.python.org/2/library/json.html?highlight=json.loads#json-to-py-table>`_).
This package works with Python 2.7+

============
Installation
============

You can install opengovpy via pip:

.. code:: shell

    $ pip install opengovpy


