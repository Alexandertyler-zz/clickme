from selenium import webdriver
from selenium.webdriver.common.by import By


i = 0
while 1:
    driver = webdriver.PhantomJS()
    driver.get('http://us.battle.net/hearthstone/en/expansions-adventures/mean-streets-of-gadgetzan/')
    driver.save_screenshot('screen.png') # save a screenshot to disk
    driver.switch_to.frame(driver.find_element(By.ID, "ngxFrame952d7ee9-d460-460b-94cd-9530b63e2c73"));
    sbtn = driver.find_element(By.XPATH, '//*[@id="xSectionDetails_xModuleGoal"]/div/div[4]')
    sbtn.click()
    driver.close()
    print i
    i += 1
