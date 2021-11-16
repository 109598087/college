from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')
url_111 = 'https://www.cac.edu.tw/cacportal/jbcrc/LearningPortfolios_MultiQuery_ppa/index.php'
driver.get(url_111)
driver.implicitly_wait(3)
driver.maximize_window()


# get discipline_cluster_list
driver.find_element(By.XPATH, "//*[contains(text(), '依學群分類查詢')]").click()
option_list = driver.find_elements(By.XPATH, "//*[@id='LPM_sel_gsdgroup']//option")

discipline_cluster_list = list()
for option in option_list:
    if '學群' in option.text and '其他' not in option.text:
        discipline_cluster_list.append(option.text)
print(discipline_cluster_list)


