108-py-protobuf-template
========================

Шаблонный репозиторий задания "Разбор потока length-prefixed Protobuf сообщений на Python" (LEARNING_CENTER-108)

Virtual environment
===================

.. code-block:: bash
    python3 -m venv venv

- unix:
.. code-block:: bash
    source venv/bin/activate

- windows:
.. code-block:: bash
    venv\Scripts\activate

.. code-block:: bash
    pip install -r requirements.txt

Build
-----

.. code-block:: bash
    python3 setup.py build

Running tests
-------------

.. code-block:: bash
    python3 -m unittest discover tests
