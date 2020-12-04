from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumCheck:
    def selenium_check(self, body, element):
        status = {"true": [], "false":[]}
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', 
        desired_capabilities=DesiredCapabilities.CHROME)
        for url in body:
            driver.get(url)
            try:
                check = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element))
            )
                status["true"].append(str(url).replace(" ","_"))
            except:
                status["false"].append(str(url).replace(" ","_"))
        driver.quit()
        return(status)