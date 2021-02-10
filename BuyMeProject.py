from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='/Users/97253/Downloads/chromedriver')
driver.implicitly_wait(3)
# Enter the website.
driver.get('http://buyme.co.il')
driver.maximize_window()
# A.Registration screen.
# Press on button.
driver.find_element_by_class_name("seperator-link").click()
# Press on button.
driver.find_element_by_class_name("text-btn").click()
# Enter first name.
driver.find_elements_by_class_name("ember-text-field")[0].send_keys("Moti")
# Enter email address.
driver.find_elements_by_class_name("ember-text-field")[1].send_keys("motilili@gmail.com")
# Enter password.
driver.find_elements_by_class_name("ember-text-field")[2].send_keys("Moti25101989L")
# Enter password again.
driver.find_elements_by_class_name("ember-text-field")[3].send_keys("Moti25101989L")
# Press button.
driver.find_element_by_class_name("ui-btn").click()
# B.Home Screen.
time.sleep(3)
driver.find_elements_by_class_name("chosen-single")[0].click()
driver.find_elements_by_class_name("active-result")[3].click()
driver.find_elements_by_class_name("chosen-single")[1].click()
driver.find_elements_by_class_name("active-result")[3].click()
driver.find_elements_by_class_name("chosen-single")[2].click()
driver.find_elements_by_class_name("active-result")[3].click()
# Press the search button.
driver.find_element_by_class_name("ui-btn").click()
# C.Choose business screen.
time.sleep(3)
# Pick a Buisness.
driver.find_elements_by_class_name("card-item")[5].click()
# Type a price.
driver.find_element_by_class_name("input-cash").send_keys("250")
driver.find_element_by_class_name("input-cash").send_keys(Keys.ENTER)
# D.Sender & Receiver information screen.
# Press radio button.
driver.find_element_by_class_name("circle").click()
# Enter receiver name.
driver.find_elements_by_class_name("ui-input")[0].send_keys("Steve Jobs")
# Enter sender name.
driver.find_elements_by_class_name("ui-input")[1].send_keys("Bill Gates")
# Enter a blessing.
driver.find_element_by_class_name("ui-textarea").send_keys("!!!FOR MY DEAR FRIEND")
# Upload a picture.
driver.find_element_by_name("fileUpload").send_keys("/Users/moti/Downloads/My Dream.jpg")
# Pick the event.
driver.find_elements_by_class_name("chosen-single")[6].click()
# Press radio button.
driver.find_elements_by_class_name("active-result")[3].click()
driver.find_element_by_xpath("//textarea[@rows='4']").clear()
driver.find_element_by_class_name("ui-textarea").send_keys("!!!FOR MY DEAR FRIEND")
driver.find_element_by_class_name("send-now").click()
# Pick Email/SMS option.
driver.find_element_by_class_name("btn-send-option-inner").click()
# Enter address/number and press save.
driver.find_elements_by_class_name("input-theme")[0].send_keys("0539996661")
driver.find_elements_by_class_name("input-theme")[1].send_keys("0536669991")
driver.find_element_by_class_name("btn-save").click()
# submit.
driver.find_element_by_class_name("submit-wrapper").click()
time.sleep(3)
driver.find_element_by_class_name("submit-wrapper").click()
driver.quit()
# Extras:
driver = webdriver.Chrome(executable_path='/Users/moti/Downloads/chromedriver')
driver.implicitly_wait(10)
driver.get('http://buyme.co.il')
driver.maximize_window()
driver.find_element_by_class_name("seperator-link").click()
driver.find_element_by_class_name("ui-btn").click()
error_messages = driver.find_elements_by_class_name("parsley-required")
for error in error_messages:
    assert error.text == "כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה"
driver.quit()
driver = webdriver.Chrome(executable_path='/Users/moti/Downloads/chromedriver')
driver.implicitly_wait(10)
driver.get('http://buyme.co.il')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.get_screenshot_as_file('/Users/moti/Downloads/screenshot.png')