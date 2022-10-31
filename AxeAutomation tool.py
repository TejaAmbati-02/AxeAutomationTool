from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_google():
    driver.get("https://www.javatpoint.com/how-to-set-python-path")
    axe = Axe(driver)
    axe.inject()
    results = axe.run()
    axe.write_results(results, 'axeIntegration.json')
    driver.close()
#     assert len(results["violations"]) == 0, axe.report(results["violations"])

test_google()
