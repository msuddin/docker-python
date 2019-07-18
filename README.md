# sample-python

## Purpose

Question: What is the purpose of this project?

Answer: To get a simple understanding of Python and how to write tests in it
* Python does not have an entry point like Java, C++, C# etc. Each line of each file is executed sequentially
* An __init__.py file is needed in each directory to allow the python interpreter to mark the directory as a module
* To understand how to write tests in Python (see Testing section below)

## Requirements
You need to have pytest installed.
```
pip install pytests
```
```
pip install pytest-bdd
```

## Instructions on running
From the root directory of the project, run the following command:
```
python sample_python.py
```
Sample Output
```
The name's Damian Wayne and my base power is 1500
The name's Bruce Wayne and my base power is 3500
Damian Wayne is not strong enough
```

## Testing
This project uses two flavours of tests.
* Python has a good selection of test runners - the built in one being UnitTest and another popular one being PyTest
* Python has a built in test library called unittest - see test/test_base_hero.py to see an example of unittest
* An example of a test written suitable for pyTest can be seen in test/test_matured_hero.py

### Running Tests

#### UnitTest Runner
You can run tests using the unittest runner (discover will be default find all tests and run them):
```
python -m unittest discover
```
Sample Output:
```
➜  sample-python git:(master) ✗ python -m unittest discover
F.
======================================================================
FAIL: test_base_hero_base_level (test.test_base_hero.TestBaseHero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mohammeduddin/Documents/GitProjects/msu/sample-python/test/test_base_hero.py", line 13, in test_base_hero_base_level
    self.assertGreater(self.__robin.get_base_level(), 1100)
AssertionError: 1000 not greater than 1100

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```
#### PyTest Runner
You can run unittest tests using PyTest runner:
```
pytest
```
Sample Output:
```
➜  sample-python git:(master) ✗ pytest
============================================================================ test session starts ============================================================================
platform darwin -- Python 2.7.15, pytest-4.6.4, py-1.8.0, pluggy-0.12.0
rootdir: /Users/mohammeduddin/Documents/GitProjects/msu/sample-python
collected 2 items                                                                                                                                                           

test/test_base_hero.py F.                                                                                                                                             [100%]

================================================================================= FAILURES ==================================================================================
__________________________________________________________________ TestBaseHero.test_base_hero_base_level ___________________________________________________________________

self = <test.test_base_hero.TestBaseHero testMethod=test_base_hero_base_level>

    def test_base_hero_base_level(self):
>       self.assertGreater(self.__robin.get_base_level(), 1100)
E       AssertionError: 1000 not greater than 1100

test/test_base_hero.py:13: AssertionError
==================================================================== 1 failed, 1 passed in 0.08 seconds =====================================================================
```

## Notes
* At the time of writing this the version of Python is: Python 2.7.15
* To use pytest as a test runner, you must install it first:
```
pip install -U pytest
```
