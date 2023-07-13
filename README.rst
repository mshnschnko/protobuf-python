108-py-protobuf-template
========================

Шаблонный репозиторий задания "Разбор потока length-prefixed Protobuf сообщений на Python" (LEARNING_CENTER-108)

Virtual environment
===================

```
    python3 -m venv venv
```

- unix:
```
    source venv/bin/activate
```

- windows:
```
    venv\Scripts\activate
```

```
    pip install -r requirements.txt
```

Build
-----

```
    python3 setup.py build
```

Running tests
-------------

```
    python3 -m unittest discover tests
```