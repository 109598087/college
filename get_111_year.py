from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')
url_111 = 'https://www.cac.edu.tw/cacportal/jbcrc/LearningPortfolios_MultiQuery_ppa/index.php'
driver.get(url_111)
driver.implicitly_wait(3)
driver.maximize_window()

# get discipline_cluster_list
driver.find_element(By.XPATH, "//*[contains(text(), '學群')]").click()
option_element_list = driver.find_elements(By.XPATH, "//*[contains(text(), '學群')]")


discipline_cluster_value_list = list()
for option_element in option_element_list:
    if option_element.get_attribute('value') is None:
        continue
    if option_element.get_attribute('value').isnumeric():
        if int(option_element.get_attribute('value')) > 0:
            discipline_cluster_value_list.append(option_element.get_attribute('value'))
print(discipline_cluster_value_list)
