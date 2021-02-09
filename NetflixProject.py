# Automation test with Selenium, for the Netflix website, the test includes registration, help buttons, links
# an existing customer, the test goes through everything.
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='/Users/97253/Downloads/chromedriver')
driver.implicitly_wait(3)
# Enter the website.
driver.get('http://netflix.com')
# Maximize window.
driver.maximize_window()
time.sleep(3)
# Scroll to the page end.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# Scroll to the page top.
driver.execute_script("window.scroll(0, 0);")
time.sleep(3)
# Registration screen.
# Enter email address.
driver.find_element_by_class_name('nfTextField').send_keys("mordechaimosheardelean@gmail.com")
# Press on button.
driver.find_element_by_class_name('cta-btn-txt').click()
# Add a password.
driver.find_element_by_name('password').send_keys("Motia25101989")
# Press on button.
driver.find_element_by_class_name('nf-btn').click()
time.sleep(3)
driver.find_element_by_class_name('submitBtnContainer').click()
# Choose plan step 2.
time.sleep(1)
driver.find_elements_by_class_name('planGrid__selectorChoice')[0].click()
time.sleep(1)
driver.find_elements_by_class_name('planGrid__selectorChoice')[1].click()
time.sleep(1)
driver.find_elements_by_class_name('planGrid__selectorChoice')[2].click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_class_name('nf-btn').click()
# Set up your payment step 3.
driver.find_element_by_class_name('mopNameAndLogos').click()
driver.find_elements_by_class_name('nfTextField')[0].send_keys("Moti")
driver.find_elements_by_class_name('nfTextField')[1].send_keys("Ardelean")
driver.find_elements_by_class_name('nfTextField')[2].send_keys("1234567890")
driver.find_elements_by_class_name('nfTextField')[3].send_keys("0125")
driver.find_elements_by_class_name('nfTextField')[4].send_keys("666")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element_by_class_name('ui-binary-input').click()
driver.find_element_by_class_name('submitBtnContainer').click()
time.sleep(2)
# Sign Out.
driver.find_element_by_class_name('authLinks').click()
driver.find_element_by_class_name('btn-logout').click()
# Sign In.
driver.find_element_by_class_name('redButton').click()
driver.find_elements_by_class_name('nfTextField')[0].send_keys("mordechaimosheardelean@gmail.com")
driver.find_elements_by_class_name('nfTextField')[1].send_keys("123456")
driver.find_element_by_class_name('hybrid-login-form-help').click()
driver.find_element_by_class_name('login-button').click()
time.sleep(1)
driver.quit()
