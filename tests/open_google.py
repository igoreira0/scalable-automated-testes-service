from config.common import TestResult
from models.test_base import TestBase

class OpenGoogle(TestBase):

    def __init__(self) -> None:
        super().__init__('Open Google', 1, 'This test should open google')

    def run(self) -> None:
        try:
            self.web_driver.get('http://www.google.com')
            self.wait_page_load()
            self.result =  TestResult.SUCCESS.value
        except:
            self.result =  TestResult.ERROR.value

    def wait_page_load(self):
        self.find_anchor_by_text("Gmail")
