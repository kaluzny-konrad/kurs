class TrainingGroundPage():
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.browser.get(self.url)
        return None

    def set_input(self, text_input):
        my_input = self.browser.find_element_by_id("ipt1")
        my_input.clear()
        my_input.send_keys(text_input)
        return None
        
    def get_input(self):
        my_input = self.browser.find_element_by_id("ipt1")
        text_input = my_input.get_attribute('value')
        return text_input

    def click_button(self):
        pass

    def quit(self):
        self.browser.quit()