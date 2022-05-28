import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Chose language')


@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
