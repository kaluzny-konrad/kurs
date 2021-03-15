#!python3

from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://techstepacademy.com/trial-of-the-stones')

task1_input = browser.find_element_by_css_selector('input[id="r1Input"]')
task1_input.send_keys('rock')
task1_button = browser.find_element_by_css_selector('button[id="r1Btn"]')
task1_button.click()

task1_output = browser.find_element_by_xpath('//div[@id="passwordBanner"]/h4')
task2_input = browser.find_element_by_css_selector('input[id="r2Input"]')
task2_input.send_keys(task1_output.text)
task2_button = browser.find_element_by_css_selector('button[id="r2Butn"]')
task2_button.click()

merchants_salary_input = browser.find_elements_by_xpath('//div/div/label[text()="Total Wealth ($):"]/../p')
max_value = 0
max_id_merchant = 0
for id, merchant_value in enumerate(merchants_salary_input):
    merchant_int_value = int(merchant_value.text)
    if merchant_int_value > max_value:
        max_id_merchant = id
        max_value = merchant_int_value

merchants_names_input = browser.find_elements_by_xpath('//div/div/label[text()="Total Wealth ($):"]/../span/b')
max_merchant_name = ''
for id, merchant_name in enumerate(merchants_names_input):
    if id == max_id_merchant:
        max_merchant_name = merchant_name.text

task3_input = browser.find_element_by_css_selector('input[id="r3Input"]')
task3_input.send_keys(max_merchant_name)
task3_button = browser.find_element_by_css_selector('button[id="r3Butn"]')
task3_button.click()

check_answer_button = browser.find_element_by_css_selector('button[id="checkButn"]')
check_answer_button.click()

check_answer_output = browser.find_element_by_xpath('//div[@id="trialCompleteBanner"]/h4')
if check_answer_output.text == 'Trial Complete':
    print('Trail Complete!')

