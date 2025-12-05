# temperature-converter-demo
Converts values between any two of the three major temperature scales: Celsius, Fahrenheit, and Kelvin.

Public repo is available here: https://github.com/Attila-Weisz/temperature-converter-demo.git

# 1. CONTENT:

## 1.1 temperature_converter.py
Converts temperatures between Celsius, Fahrenheit, and Kelvin.
- One given temperature is converted into the other two units, and then the results are printed.
- Includes TemperatureConverter class with six converter functions, and also includes main() function.

## 1.2 test_unit_temperature_converter.py
Unit tests for TemperatureConverter class methods.

Each of the six methods is tested with known input-output pairs.

## 1.3 test_integration_temperature_converter.py
Tests the convert_and_print method for Celsius input: 0 C should convert to 32 F and 273.15 K.

Tests the roundtrip conversion from Celsius to Fahrenheit and back: 25 C should convert to 77 F and back to approximately 25 C.

## 1.4 master-all-tests.yml
CI pipeline:
- Workflow called "Main All Tests" runs on push actions (and not on pull request action) on Main/Master branch.
- There is only one job to it: "all-tests".
- Runs on Ubuntu Linux virtual machine in GitHub.
- It clones repo and installs Python 3.13, together with pytest module.
- It runs the following tests in this order:
    - unit tests
    - integration tests

## 1.5 pr-unit-test.yml
CI pipeline:
- Workflow called "PR Unit Tests" runs when someone opens/updates a pull request into Main/Master branch.
- There is only one job to it: "unit-tests".
- Runs on Ubuntu Linux virtual machine in GitHub.
- It clones repo and installs Python 3.13, together with pytest module.
- It only runs the following tests:
    - unit tests

# 2. DEPLOYMENT INC. TESTS:

This project uses [pytest](https://docs.pytest.org/) for testing.
```bash
pytest tests/test_unit_temperature_converter.py
pytest tests/test_integration_temperature_converter.py
```

## STEP 1:
```yml
cd <target/folder>
git clone https://github.com/Attila-Weisz/temperature-converter-demo.git
cd temperature-converter-demo
git add .
git commit -m "Initial commit with converter and tests"
git push origin main
```

Check if Main All Tests have completed or not in "Actions / Main All Tests"

==> YES, tick in green

## STEP 2:
New branch for unit test FAIL:
```bash
git checkout -b feature/fail-test
```
Unit test changed to force a failure: assert TemperatureConverter.celsius_to_fahrenheit(0.0) == pytest.approx(92.0)
```bash
git add tests/test_unit_temperature_converter.py
git commit -m "Make unit test fail for demo purposes"
git push origin feature/fail-test
```
**Create pull request** `feature/fail-test` → `master/main`

Check if PR Unit Tests have completed or not in "Actions / PR Unit Tests"

==> NO, x in red

## STEP 3:
New branch for unit test PASS:
```bash
git checkout -b feature/pass-test
```
Unit test changed back to correct value to pass: assert TemperatureConverter.celsius_to_fahrenheit(0.0) == pytest.approx(32.0)
```bash
git add tests/test_unit_temperature_converter.py
git commit -m "Make unit test pass (again) for demo purposes"
git push origin feature/pass-test
```
**Create pull request** `feature/pass-test` → `master/main`

Check if PR Unit Tests have completed or not in "Actions / PR Unit Tests"
==> YES, tick in green
