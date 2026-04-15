import time
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)

    # Находим кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяе видимость кнопки в контексте товара
    assert button.is_displayed()
