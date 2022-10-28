import pymongo
import time
from abc import ABC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.constants import MONGODB_TESTS_COLLECTION
from utils.mongo_adapter_factory import create_database_connection

mongo = create_database_connection(MONGODB_TESTS_COLLECTION)

class TestBase(ABC):

    def __init__(self, name, id, description) -> None:
        self.name = name
        self.id = id
        self.description = description
        self.web_driver = webdriver.Chrome(ChromeDriverManager().install())
        self.start = time.time()
        self.end = None
        self.result = None

    def close(self):
        self.end = time.time()
        self.web_driver.close()
        mongo.insert_one(
            {
                'test_name': self.name,
                'test_id': self.id,
                'test_description': self.description,
                'start_time': self.start,
                'end_time': self.end,
                'result': self.result
            }
        )

    def wait_for_element_by_xpath(self, selector: str, timeout: int = 300, poll_frequency: int = 2) -> None:
        WebDriverWait(self.web_driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda d: d.find_element(By.XPATH, selector).is_displayed())
        return self.web_driver.find_element(By.XPATH, selector)

    def find_element_by_xpath(self, selector):
        return self.web_driver.find_element(By.XPATH, selector)

    def find_anchor_by_text(self, text):
        return self.web_driver.find_element(By.XPATH, f"//a[contains(text(),'{text}')]")
