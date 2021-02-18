from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    # go to google.com
    driver.get('https://google.com')
    # type in a search 'qa jobs'
    driver.find_element(By.NAME, 'q').send_keys('qa jobs')
    # submit or enter the search
    driver.find_element(By.NAME, 'btnK').submit()
    # assert we got a search page for qa jobs
    assert 'qa jobs' in driver.title
