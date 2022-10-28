from config.common import TestResult
from models.test_base import TestBase

class GenericTest(TestBase):
    
    def __init__(self) -> None:
        super().__init__('Generic Test', 2, 'This test should test a generic webpage')

    def run(self) -> None:
        try:
            self.web_driver.get('https://tangjiajia666.github.io/web-deisgn/')
            self.wait_for_element_by_xpath("//span[contains(text(),'HTML5')]")
            self.find_anchor_by_text("Home")
            self.find_anchor_by_text("About")
            self.find_anchor_by_text("Services")
            self.find_element_by_xpath("//input[@type='email']")
            self.find_element_by_xpath("//button[@type='submit']")
            self.result =  TestResult.SUCCESS.value
        except:
            self.result =  TestResult.ERROR.value