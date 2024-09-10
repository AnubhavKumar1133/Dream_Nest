from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

def setup_method():
    global driver
    driver = webdriver.Chrome()

def teardown_method():
    global driver
    driver.quit()

def test_sample():
    driver.get("http://localhost:3000/login")
    driver.set_window_size(1552, 832)
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").send_keys("login@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("login")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    driver.find_element(By.LINK_TEXT, "Become A Host").click()
    driver.find_element(By.CSS_SELECTOR, ".category:nth-child(6) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".type:nth-child(1)").click()
    driver.find_element(By.NAME, "streetAddress").click()
    driver.find_element(By.NAME, "streetAddress").send_keys("Big Ben")
    driver.find_element(By.NAME, "aptSuite").send_keys("Markenshire")
    driver.find_element(By.NAME, "city").send_keys("London")
    driver.find_element(By.NAME, "province").send_keys("NA")
    driver.find_element(By.NAME, "country").send_keys("England")
    driver.find_element(By.NAME, "city").click()
    driver.find_element(By.NAME, "city").click()
    element = driver.find_element(By.NAME, "city")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, "city").send_keys("Strappen")
    driver.find_element(By.NAME, "province").send_keys("London")
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(2) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(2) .MuiSvgIcon-root:nth-child(3) > path").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(2) .MuiSvgIcon-root:nth-child(3) > path")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(2) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(3) .MuiSvgIcon-root:nth-child(3) > path")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(1) .MuiSvgIcon-root:nth-child(3) > path")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(4) .MuiSvgIcon-root:nth-child(3)").click()
    element = driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(4) .MuiSvgIcon-root:nth-child(3)")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(4) .MuiSvgIcon-root:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(4) .MuiSvgIcon-root:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".basic:nth-child(4) .MuiSvgIcon-root:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".facility:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".facility:nth-child(15)").click()
    driver.find_element(By.CSS_SELECTOR, ".facility:nth-child(23) > p").click()
    driver.find_element(By.CSS_SELECTOR, ".facility:nth-child(24) > .facility_icon").click()
    driver.find_element(By.CSS_SELECTOR, ".facility:nth-child(27)").click()
    driver.find_element(By.NAME, "title").click()
    driver.find_element(By.NAME, "title").send_keys("Pools are the View")
    driver.find_element(By.CSS_SELECTOR, "textarea:nth-child(4)").send_keys("The Pools on the rooftop and the view from there is awesome")
    driver.find_element(By.NAME, "highlight").send_keys("The city and the place you are staying is the highlight")
    driver.find_element(By.NAME, "highlightDesc").send_keys("worth the money")
    driver.find_element(By.NAME, "price").send_keys("99")
    driver.find_element(By.CSS_SELECTOR, ".submit_btn").click()
    driver.find_element(By.CSS_SELECTOR, ".css-h081rb-MuiSvgIcon-root").click()
    driver.find_element(By.LINK_TEXT, "Trip List").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar_right_account").click()
    driver.find_element(By.LINK_TEXT, "Property List").click()

setup_method()
test_sample()
teardown_method()
