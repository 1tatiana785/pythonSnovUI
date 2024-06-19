import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import os


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    perfs = {"download.defoult_directory": f"{os.getcwd()}/downloads"}
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("prefs", perfs)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    #service = Service(f"{os.getcwd()}/chromedriver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), executable_path=(f"{os.getcwd()}/chromedriver"), options=options)
    request.cls.driver = driver  # create object driver in tests classes
    yield driver  # return driver
    driver.quit()
