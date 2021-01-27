# Code Exam
Task Description provided

### General
- Include a readme with instructions on how to install and run your tests
- Submit your code to a public GitHub repo or similar
- You can choose to either do UI Automation or API Automation, or you can do both to highlight your skillset
- Bonus points for:
    - Utilize webdriver.io (UI)
    - Utilize a linter
    - Run more than one test in parallel
    - Run tests both with a head and headless (UI)
    - Create Docker image to run tests in
    - Setup a pipeline using Gitlab to run your tests

### UI Automation
Using preferred language, write UI automation against www.saucedemo.com
- Workflow:
	- Log into the site
	- Sort the items (Lowest Price sort) 
	- Add two or more items to the shopping cart
	- Visit the shopping cart
		- Assert that the items that you added are in the cart
	- Remove an item and then continue shopping
	- Add another item
	- Checkout
		- Assert you are purchasing the correct items
		- Assert the total price
		- Finish checkout
- What we are going to look at:
	- Does the code function properly and follow the workflow
	- How are you selecting elements
	- How are you waiting for elements to load
	- Error Handling (Assertions, Logging, etc.)
	- Code structure and design
		- How modular is your code
		- Neatness counts


## Project structure (Framework)

Page object modeling design pattern is used in this project. Each page/window/frame has its own page.py file with necessary class(es) in it.
Classes can inherit if window/panels are part of bigger frame.
Tests are set up with pytest Testing Framework and test should be run using pytest. Pytest should be added to PATH to run the test without python -m extension.

See the following notes next to Framework components.

```
ecommerce
- data                      (input data file directory)
    - configs.yaml          (properties file for main parameters, especially for the fixture file)
    - ...
- logs                      (daily logs directory, log files with .log extention)
- reports                   (html or other reports directory)
- screenshots               (screenshots taken during the run, this can be managed better way or with reporting plugin)
- src                       (main source package)
    - pages                 (package for all page factories - elements and necessary funtions)
        - base_page.py      (abstract pages that implements driver, selenium methods)
        - ...
    - steps                 (package for steps functions that used page objects)
        - login_steps.py    
        - ...
    - tests                 (package for test scenarios)
        - test_main.py      (test scenario module executable with pytest)
        - ...
- all_imports.py            (reusable imports module for test scenarios)
- conftest.py               (pytest fixture module that includes SetUp and TearDown for test scenarios)
- utilities.py              (commonly used generic methods, can be used anywhere in the framework)

```

**NOTE: This framework can be converted to BDD framework using pystest-bdd or behave plugins. "src/features" directory is added with sample gherkin file. Functions Under steps package can be used as step definitions (with ghekin Given/When/Then steps can be mapped to python functions.). This will change the running steps.**

## Instructions 
#### Necessary package installation:

Required packages are listed in the requirements.txt which can be installed as follows.
```shell script
$ pip install -r requirements.txt --no-index
```
#### Running tests
Test scenarios and fixture are set up for pytest testing framework. Test scenarios or Test Suites can be executed from command line as follows:

```shell script
# all tests under project 
pytest

# specific test module
pytest src/tests/test_main.py

# specific test scenario
pytest src/tests/test_main.py::test_login

# test or group of tests that are marked as 'smoke'
pytest -m smoke 

```
#### Parallel Test Execution with Pytest  
To run the tests parallel pytest-xdist plugin is needed. Here’s how to run the example project with 4 test threads:
```shell script
$ pipenv run python -m pytest -n 4
```

