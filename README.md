# Selenium Test for Language Selection and Button Visibility

This repository contains a test suite that validates the functionality of a product page on a website. The test ensures that the browser is launched with the specified user language, and it verifies that the "Add to Basket" button is present on the product page.

## Project Structure

- **conftest.py**: Contains the logic to launch the browser with the user-specified language. The browser is declared in a fixture and passed to the test as a parameter.
- **test_items.py**: Contains the test that checks if the "Add to Basket" button is present on the product page.

## Requirements

- Python 3.x
- Selenium
- pytest
