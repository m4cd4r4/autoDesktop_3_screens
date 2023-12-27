"""
Script: Bunnings Office - Automated Log-ins + Desktop Apps & Browser Windows layout 
Version: v1.0
Author: m4cd4r4
Date: 15/01/2023

Dependencies:
Install Selenium: pip install -U selenium
Install WebDriver for Edge Browser: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
"""

from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By 
from selenium import webdriver


browser = webdriver.Edge()

# Okta Admin
browser.get("https://team-login.bunnings.com.au")
while(True):
    pass    # stops the browser window from closing once the script has finished running


# Pause the script to wait for page elements to load
# time.sleep(3)

# Locate the button and click on it
# https://stackoverflow.com/questions/73325794/how-to-click-on-button-using-selenium
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='okta-signin-submit']"))).click()
#button  = driver.find_element("xpath", "//*[@id='okta-signin-submit']")
#button.click()

