from config.common import TestResult
from models.test_base import TestBase

class GenericTestError(TestBase):
    
    def __init__(self) -> None:
        super().__init__('Generic Test Error', 3, 'This test should test a generic webpage')

    def run(self) -> None:
        try:
            self.web_driver.get('https://tangjiajia666.github.io/web-deisgn/')
            self.wait_for_element_by_xpath("//span[contains(text(),'HTML5')]")
            self.find_element_by_xpath("//a[contains(text(),'Home')]")
            self.find_element_by_xpath("//a[contains(text(),'About')]")
            self.find_element_by_xpath("//a[contains(text(),'Services')]")
            self.find_element_by_xpath("//input[@type='email']")
            self.find_element_by_xpath("//button[@type='submit12']")
            self.result =  TestResult.ERROR.value
        except:
            self.result =  TestResult.SUCCESS.value