from selenium import webdriver
from selenium.webdriver.common.by import By

def test_ice_spirit_is_displayed():
    driver = webdriver.Chrome()
    # go to statsroyale.com
    driver.get('https://statsroyale.com')

    # go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # assert Ice Spirit is displayed
    ice_spirit_card = driver.find_element(By.NAME, "[href*='Ice+Spirit']")
    assert ice_spirit_card.is_displayed
 