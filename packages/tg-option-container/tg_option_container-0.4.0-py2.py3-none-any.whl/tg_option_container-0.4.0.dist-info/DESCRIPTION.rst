tg-option-container
===================

|Build Status| |Coverage Status| |PyPI Status|

Container for dictionary-like validated data structures

Documentation is available on Read the Docs:
http://tg-option-container.readthedocs.io

Getting started
---------------

Install tg-option-container:

.. code:: sh

    pip install tg-option-container

Then use it in your project:

.. code:: python

    from tg_option_container import Option, OptionContainer


    class Character(OptionContainer):
        props = [
            Option.string('name', None),
            Option.string('gender', None, choices=('M', 'N')),
        ]


    john = Character(name='John Smith', gender='M')

    # This will raise: tg_option_container.types.InvalidOption: Invalid choice x for option `gender`, choices are ('M', 'N').
    mary = Character(name='Mary Smith', gender='x')

Development
-----------

You can run the tests by running ``tox`` in the top-level of the
project.

.. |Build Status| image:: https://travis-ci.org/thorgate/tg-option-container.svg
   :target: https://travis-ci.org/thorgate/tg-option-container
.. |Coverage Status| image:: https://codecov.io/gh/thorgate/tg-option-container/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/thorgate/tg-option-container
.. |PyPI Status| image:: https://badge.fury.io/py/tg-option-container.png
   :target: https://badge.fury.io/py/tg-option-container


