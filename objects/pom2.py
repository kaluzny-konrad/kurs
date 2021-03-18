from selenium import webdriver
from training_ground_page import TrainingGroundPage

# set variables
browser = webdriver.Chrome('chromedriver.exe')
input_text = 'testowy input'

# perform an action on the page
page = TrainingGroundPage(browser)
page.go()
page.set_input(input_text)
page_input = page.get_input()
page.quit()

# test
error_text = f"Values are diff\nSet: {input_text}"
error_text += f"\nGet: {page_input}"
assert page_input == input_text, error_text