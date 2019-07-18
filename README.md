# sample-docker-python

## Purpose

Question: What is the purpose of this project?

Answer: To get a simple understanding of Python and how to write tests in it
* Python does not have an entry point like Java, C++, C# etc. Each line of each file is executed sequentially
* An __init__.py file is needed in each directory to allow the python interpreter to mark the directory as a module
* To understand how to write tests in Python (see Testing section below)
* To run the tests insigh a docker container (via both Dockerfile and docker-compose.yml)

## Requirements
You need to have pytest installed.
```
pip install pytests
```
```
pip install pytest-bdd
```

## Instructions on running
### Running the sample script
From the root directory of the project, run the following command (this is an example of running a python script):
```
python3 sample_python.py
```
Sample Output
```
The name's Damian Wayne and my base power is 1500
The name's Bruce Wayne and my base power is 3500
Damian Wayne is not strong enough
```

### Testing
This project uses two flavours of tests.
* Python has a good selection of test runners - the built in one being UnitTest and another popular one being PyTest
* Python has a built in test library called unittest - see test/test_base_hero.py to see an example of unittest
* An example of a test written suitable for pyTest can be seen in test/test_matured_hero.py

#### Running Tests

##### UnitTest Runner
You can run tests using the unittest runner ('discover' will by default find all tests and run them):
```
python3 -m unittest discover
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
##### PyTest Runner
You can run unittest tests using PyTest runner (PyTest by default is also able to run any test written with unittest in mind):
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

### Docker
This project uses docker to run all tests inside a container.
Please note that both commands at present will fail since out of the 5 tests, two are failing. 
If all tests pass, the both will succeed and the images will be built and running.

#### Dockerfile
You can run all the tests by building a docker container as outlined in the Dockerfile:
```
docker build .
```
Sample Output
```
➜  sample-python git:(master) docker build .
Sending build context to Docker daemon  9.176MB
Step 1/4 : FROM python
 ---> 42d620af35be
Step 2/4 : COPY . ./sample-python/.
 ---> 3c924c495142
...
...
...
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /sample-python
collected 5 items

test/test_base_hero.py F.                                                [ 40%]
test/test_matured_hero.py ..F                                            [100%]

=================================== FAILURES ===================================
____________________ TestBaseHero.test_base_hero_base_level ____________________

self = <test.test_base_hero.TestBaseHero testMethod=test_base_hero_base_level>

>   ???
E   AssertionError: 1000 not greater than 1100

/Users/mohammeduddin/Documents/GitProjects/msu/sample-python/test/test_base_hero.py:13: AssertionError
___________________________ test_matured_hero_power ____________________________

>   ???
E   AssertionError: assert 'Fear Factor' == 1000
E    +  where 'Fear Factor' = <bound method MaturedHero.get_power of <application.matured_hero.MaturedHero object at 0x7fbab9d6c950>>()
E    +    where <bound method MaturedHero.get_power of <application.matured_hero.MaturedHero object at 0x7fbab9d6c950>> = <application.matured_hero.MaturedHero object at 0x7fbab9d6c950>.get_power

/Users/mohammeduddin/Documents/GitProjects/msu/sample-python/test/test_matured_hero.py:16: AssertionError
====================== 2 failed, 3 passed in 0.04 seconds ======================
The command '/bin/sh -c pip3 install pytest && pytest' returned a non-zero code: 1
```

#### docker-compose.yml
You can use the docker compose method to start up an actual process:
```
docker-compose up
```
Sample Output:
```
➜  sample-python git:(master) docker-compose up
Building sample_python
Step 1/4 : FROM python
...
...
....
Step 2/4 : COPY . ./sample-python/.
 ---> e92650ac0a4c
Step 3/4 : WORKDIR sample-python
 ---> Running in b5071adafa89
...
...
...
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /sample-python
collected 5 items

test/test_base_hero.py F.                                                [ 40%]
test/test_matured_hero.py ..F                                            [100%]

=================================== FAILURES ===================================
____________________ TestBaseHero.test_base_hero_base_level ____________________

self = <test.test_base_hero.TestBaseHero testMethod=test_base_hero_base_level>

>   ???
E   AssertionError: 1000 not greater than 1100

/Users/mohammeduddin/Documents/GitProjects/msu/sample-python/test/test_base_hero.py:13: AssertionError
___________________________ test_matured_hero_power ____________________________

>   ???
E   AssertionError: assert 'Fear Factor' == 1000
E    +  where 'Fear Factor' = <bound method MaturedHero.get_power of <application.matured_hero.MaturedHero object at 0x7fa117834a90>>()
E    +    where <bound method MaturedHero.get_power of <application.matured_hero.MaturedHero object at 0x7fa117834a90>> = <application.matured_hero.MaturedHero object at 0x7fa117834a90>.get_power

/Users/mohammeduddin/Documents/GitProjects/msu/sample-python/test/test_matured_hero.py:16: AssertionError
====================== 2 failed, 3 passed in 0.04 seconds ======================
ERROR: Service 'sample_python' failed to build: The command '/bin/sh -c pip3 install pytest && pytest' returned a non-zero code: 1

```

## Notes
* At the time of writing this the version of Python is: Python 2.7.15
* To use pytest as a test runner, you must install it first (see Dockerfile):
```
pip3 install -U pytest
```
