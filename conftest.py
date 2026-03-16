import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Language interface")

@pytest.fixture
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_argument(f"--lang={user_language}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
