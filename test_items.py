import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def wait_for_element_to_be_clickable_and_visible(
    browser, by, value, timeout=10, max_attempts=3
):
    """Wait for an element to be clickable and visible, with retry attempts."""
    attempt = 0
    while attempt < max_attempts:
        try:
            print(f"Attempt {attempt + 1} to locate element '{value}'...")
            element = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except NoSuchElementException:
            print(f"NoSuchElement: Element '{value}' does not exist on a page.")
            return None
        except TimeoutException:
            print(
                f"Timeout: Element '{value}' not found within {timeout} seconds on attempt {attempt + 1}."
            )
            attempt += 1
            time.sleep(3)
        except Exception as e:
            print(f"An unexpected error occurred on attempt {attempt + 1}: {e}")
            attempt += 1
    print(f"Failed to locate element '{value}' after {max_attempts} attempts.")
    return None


def test_button_existence_for_selected_language(browser, request):
    # Get the language from pytest options
    user_language = request.config.getoption("language")
    try:
        browser.get(link)
        select = Select(browser.find_element(By.CLASS_NAME, "form-control"))
        select.select_by_value(user_language)
        selected_option = select.first_selected_option
        time.sleep(5)

        assert (
            selected_option.get_attribute("value") == user_language
        ), f"Expected language '{user_language}' but got '{selected_option.get_attribute('value')}'."
        print(f"Language '{user_language}' successfully selected.")

        submit_button = wait_for_element_to_be_clickable_and_visible(
            browser=browser,
            by=By.CSS_SELECTOR,
            value="#add_to_basket_form button.btn.btn-lg.btn-primary.btn-add-to-basket",
            timeout=10,
            max_attempts=3,
        )

        assert submit_button is not None, "Submit button was not found."
        assert submit_button.is_displayed(), "Submit button is not visible."
        assert submit_button.is_enabled(), "Submit button is not clickable."

        print("Submit button is visible and clickable.")
    except Exception as e:
        print(f"Test failed: {e}")
        raise
