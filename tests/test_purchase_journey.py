"""Automation practice code question 1"""
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    # Set up the WebDriver instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown - Quit the WebDriver instance
    driver.quit()


def test_purchase_journey(driver):

    try:
        wait = WebDriverWait(driver, 10)
        driver.get('http://automationpractice.pl/index.php')

        driver.maximize_window()

        # Click Sign in
        sign_in_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login')
        ))
        sign_in_button.click()

        # Enter email
        username = wait.until(EC.presence_of_element_located(
            (By.ID, 'email')
        ))
        username.send_keys('testautomationmfs@gmail.com')

        # Enter password
        password = driver.find_element(
            By.CSS_SELECTOR, '[data-validate="isPasswd"]')
        password.send_keys('TestAutomation@123')

        # Click Sign In button
        driver.find_element(By.ID, 'SubmitLogin').click()

        # Locate Home button after login in to the platform
        home_auth_link = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'Home')
        ))

        # Scroll down to Home button
        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);", home_auth_link)

        # Click Home button to go back to the landing page
        home_auth_link.click()

        # Locate popular category
        popular_category = wait.until(EC.presence_of_element_located(
            (By.ID, 'homefeatured')
        ))

        # Scroll to popular category
        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);", popular_category)

        # Locate women category
        women = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'WOMEN')
        ))

        # Mouse hover on women category
        hover_dresses_category = ActionChains(driver)
        hover_dresses_category.move_to_element(women)
        hover_dresses_category.perform()

        # Locate and click on evening dresses
        evening_dresses = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'Evening Dresses')
        ))
        evening_dresses.click()

        # Filter by M size
        m_size_checkbox = wait.until(EC.presence_of_element_located(
            (By.ID, 'layered_id_attribute_group_2')
        ))
        m_size_checkbox.click()

        # Choose color pink
        pink_color = driver.find_element(
            By.CSS_SELECTOR, '[data-rel="24_3"]')
        pink_color.click()

        time.sleep(9)
        # Locate price range slider
        price_range_slider = driver.find_element(By.ID, "layered_price_slider")

        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);", price_range_slider)

        time.sleep(8)
        # Filter by price range
        drag_slider = ActionChains(driver)
        drag_slider.drag_and_drop_by_offset(
            price_range_slider, 65, 0).perform()
        time.sleep(4)
        drag_slider.release().perform()

        # Locate printed dress
        printed_dress = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'Printed Dress')

        ))
        # Mouse over printed dress
        hover_printed_dress = ActionChains(driver)
        hover_printed_dress.move_to_element(printed_dress)
        hover_printed_dress.perform()

        # Locate More button and click on it
        view_button = wait.until(EC.presence_of_element_located(

            (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a')

        ))
        view_button.click()

        time.sleep(10)

        # Locate quantity label

        quantity_label = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="quantity_wanted_p"]/label')
        ))

        # Let's see if quantity label is displayed

        is_quantity_label_displayed = quantity_label.is_displayed()
        is_product_available = is_quantity_label_displayed

        print("Product quantity label is displayed: ",
              is_quantity_label_displayed)

        # CHECK PRODUCT AVAILABILITY STATUS
        # Locate the product availability span
        products_availability_value = driver.find_element(
            By.ID, 'availability_value')

        availability_text = products_availability_value.text
        print(availability_text)

        is_product_availability_displayed = products_availability_value.is_displayed()
        print(
            "Product availability is displayed: ", is_product_availability_displayed)

        if availability_text == "This product is no longer in stock" or not is_product_available:
            print("The product seems to be no more in stock. "
                  "We can't pursue the purchase journey.")
        else:
            print("Let's continue")

        time.sleep(10)

    finally:

        driver.quit()
