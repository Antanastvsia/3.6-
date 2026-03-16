import time
from selenium.webdriver.common.by import By

def test_button_add_to_cart_exists(browser):
    """
    Тест проверяет наличие кнопки добавления в корзину на странице товара.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Задержка для визуальной проверки языка
    time.sleep(30)
    
    # Поиск кнопки внутри формы add_to_basket_form
    button = browser.find_element(By.CSS_SELECTOR, "form#add_to_basket_form button[type='submit']")
    
    # Проверка, что кнопка отображается
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена"
