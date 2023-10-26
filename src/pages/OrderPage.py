from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def remove_items(self):
        try:
            remove = WebDriverWait(self.driver, 10).until(

                EC.presence_of_element_located((By.XPATH, "//tbody/tr[2]/td[6]/a[1]"))
            )
            assert remove.is_displayed(), "cart input is not displayed on the page."
            remove.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def continoue(self):
        try:
            xyz = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'btnSubmit')])[2]"))
            )
            assert xyz.is_displayed(), "continoue button is not displayed on the page."
            xyz.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_on_cart_again(self):
                try:
                    cart = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@href='/cart']"))
                    )
                    assert cart.is_displayed(), "cart input is not displayed on the page."
                    cart.click()

                except Exception as e:
                    print(f"Assertion failed")

    def click_on_Buy_now(self):
        try:
            buy_now = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@value,'Buy Now')]"))
            )
            assert buy_now.is_displayed(), "buy now button is not displayed on the page."
            buy_now.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_on_home(self):
        try:
            home = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[contains(@value,'Home')])[2]"))
            )
            assert home.is_displayed(), "HOME button is not displayed on the page."
            home.click()

        except Exception as e:
            print(f"Assertion failed: {e}")
