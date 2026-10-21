
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.saucedemo.com/")

    yield browser

    browser.quit()


def login(driver, username="standard_user",
          password="secret_sauce"):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# TC01: Dang nhap thanh cong
def test_valid_login(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    assert "inventory" in driver.current_url


# TC02: Dang nhap sai mat khau
def test_invalid_login(driver):
    login(driver, password="wrong_password")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Username and password do not match" in error.text


# TC03: Sap xep gia tang dan
def test_sort_price_low_to_high(driver):
    login(driver)

    sort_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "product_sort_container")
        )
    )
    sort_dropdown.send_keys("Price (low to high)")

    WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )[0].text == "$7.99"
    )

    prices = [
        float(item.text.replace("$", ""))
        for item in driver.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )
    ]

    assert prices == sorted(prices)


# TC04: Them san pham vao gio hang
def test_add_product_to_cart(driver):
    login(driver)

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    add_button.click()

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1"


# TC05: Dang xuat
def test_logout(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    assert driver.current_url.rstrip("/").endswith("saucedemo.com")
