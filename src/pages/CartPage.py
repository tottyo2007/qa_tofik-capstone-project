from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_cart(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/cart']"))
            )
            assert cart.is_displayed(), "cart input is not displayed on the page."
            cart.click()

        except Exception as e:
            print(f"Assertion failed")

