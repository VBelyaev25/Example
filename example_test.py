import unittest
from selenium import webdriver
from openpyxl import load_workbook
from methods_for_login import login

class ExampleTest(unittest.TestCase):

    def setUp(self):
        self.test_val = load_workbook('cfg.xlsx')
        self.sheet_for_path = self.test_val.get_sheet_by_name('Path')
        self.driver = webdriver.Firefox(executable_path = self.sheet_for_path['A1'].value)
        self.driver.get(self.sheet_for_path['A2'].value)

    def tearDown(self):
        self.driver.close()
        self.test_val.close()

    def check_result(self, result):
        result.find_element_by_class_name('widget-button__Avatar-sc-7ezmr3-6').click()
        assert 'Профиль' in result.page_source
        assert 'Выход' in result.page_source


    def test_login_classic(self):
        logIn = login(self.driver, self.test_val)
        logIn.Singin()
        result = logIn.RegistrationClassic()
        self.check_result(result)

    def test_login_vk(self):
        logIn = login(self.driver, self.test_val)
        logIn.Singin()
        result = logIn.RegistrationVK()
        self.check_result(result)

    def test_login_facebook(self):
        logIn = login(self.driver, self.test_val)
        logIn.Singin()
        result = logIn.RegistrationFacebook()
        self.check_result(result)

if __name__ == '__main__':
    unittest.main()