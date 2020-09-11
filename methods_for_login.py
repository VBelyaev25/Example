from methods_for_email import GetCodeIntoEmail
import time

class login():
    def __init__(self, driver, load_workbook):
        self.driver = driver
        self.test_val = load_workbook

    def Singin(self):
        self.driver.find_element_by_class_name('button__View-sc-1yof2fx-0').click()
        self.regisstration = False

    def EnterCode(self, sheet, flag):
        code = GetCodeIntoEmail(sheet['A1'].value, sheet['B1'].value).getEmail()
        self.driver.find_element_by_class_name('input__InputHtml-sc-185agi7-3').send_keys(code)
        self.driver.find_element_by_class_name('button-action__View-sc-1xgnbfo-0').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('link__View-sc-1ydrjtx-0').click()
        if flag == False:
            self.driver.find_element_by_class_name(
            'input__InputHtml-sc-185agi7-3').send_keys(sheet['C1'].value)
        self.driver.find_element_by_class_name('radio__Button-sc-1o8grr6-1').click()
        self.driver.find_element_by_class_name('buttonLoader__View-hkgzw7-0').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('buttonLoader__View-hkgzw7-0').click()
        self.driver.find_element_by_xpath('//div[3]//div[1]//div[3]/button').click()

    def RegistrationClassic(self):
        try:
            sheet = self.test_val.get_sheet_by_name('Val')
            self.driver.find_element_by_class_name('link__View-sc-1ydrjtx-0').click()
            self.driver.find_element_by_xpath(
                '//div[3]//div[1]//fieldset[1]//div[2]/input').send_keys(sheet['A1'].value)
            self.driver.find_element_by_xpath(
                '//div[3]//div[1]//fieldset[2]//div[2]/input').send_keys(sheet['B1'].value)
            self.driver.find_element_by_class_name('buttonLoader__View-hkgzw7-0').click()
            self.EnterCode(sheet, False)
            self.regisstration = True
        finally:
            return self.FinallyAction()

    def RegistrationVK(self):
            sheet = self.test_val.get_sheet_by_name('Val')
            try:
                self.driver.find_element_by_xpath('//button[2]/img').click()
                old_window, new_window = self.driver.window_handles
                self.SwitchToWindow(new_window, False, sheet)
                self.driver.find_element_by_xpath('//div[2]//input[6]').send_keys(sheet['A2'].value)
                self.driver.find_element_by_xpath('//div[2]//input[7]').send_keys(sheet['B2'].value)
                self.driver.find_element_by_xpath('//*[@id="install_allow"]').click()
                self.SwitchToWindow(old_window, 'VK', sheet)
                self.EnterCode(sheet, True)
                self.regisstration = True
            finally:
                return self.FinallyAction()

    def RegistrationFacebook(self):
        sheet = self.test_val.get_sheet_by_name('Val')
        try:
            self.driver.find_element_by_xpath('//div[1]//div[1]/div[2]/button[1]/img').click()
            old_window, new_window = self.driver.window_handles
            self.SwitchToWindow(new_window, False, sheet)
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(sheet['A3'].value)
            self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(sheet['B3'].value)
            self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
            self.SwitchToWindow(old_window, 'FB', sheet)
            self.EnterCode(sheet, True)
            self.regisstration = True
        finally:
            return self.FinallyAction()

    def SwitchToWindow(self, window, flag, sheet):
        self.driver.switch_to_window(window)
        if flag == 'FB':
            time.sleep(3)
            self.driver.find_element_by_xpath('//label/div[2]/input').send_keys(sheet['A1'].value)
            self.driver.find_element_by_class_name('button-action__View-sc-1xgnbfo-0').click()
        if flag == 'VK':
            time.sleep(3)
            self.driver.find_element_by_xpath('//label/div[2]/input').send_keys(sheet['A1'].value)
            self.driver.find_element_by_xpath('//div[3]//div[1]/button[1]').click()

    def FinallyAction(self):
        assert self.regisstration, True
        self.test_val.close()
        return self.driver