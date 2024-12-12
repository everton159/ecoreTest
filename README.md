# ecareTest

This project is a Selenium-based automated testing suite for ecare interview.

## Features

- Login Tests
- invoice test
## Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver
- Dependencies specified in the `requirements.txt` file

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/everton159/ecareTest
   cd ecareTest

2. Install requirements
    ```bash
    pip install -r requirements.txt

3. How to run
    ```bash
    #Entire project
    python -m unittest discover -s tests
    #specific feature
    python -m unittest tests.test_login
    #specific test scenario
    python -m unittest tests.test_login.TestLogin.test_login_positive

