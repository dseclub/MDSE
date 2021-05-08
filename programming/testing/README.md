## Testing with Pytest

Pytest is a testing framework based on python. It is mainly used to write API test cases.

**Fixtures** for handling test dependencies, state, and reusable functionality
**Marks** for categorizing tests and limiting access to external resources
**Parametrization** for reducing duplicated code between tests
**Durations** to identify your slowest tests
**Plugins** for integrating with other frameworks and testing tools




 ```
pytest -vs tests/mark_parametrization.py

pytest -vv tests/mark_parametrization.py
pytest -q test_try.py

pytest --fixtures   # shows builtin and custom fixtures
 ```


https://docs.pytest.org/en/6.2.x/

https://realpython.com/pytest-python-testing/

https://code.visualstudio.com/docs/python/testing



## Books

Python Testing with pytest Simple, Rapid, Effective, and Scalable by Brian Okken

Test–Driven Development with Python 2e
