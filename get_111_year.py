import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd


def get_option_value_list(option_element_list):
    value_list = list()
    for option_element in option_element_list:
        if option_element.get_attribute('value') is None:
            continue
        if option_element.get_attribute('value').isnumeric():
            if int(option_element.get_attribute('value')) >= 0:
                value_list.append(option_element.get_attribute('value'))
    return value_list


driver = webdriver.Chrome('chromedriver.exe')
url_111 = 'https://www.cac.edu.tw/cacportal/jbcrc/LearningPortfolios_MultiQuery_ppa/index.php'
driver.get(url_111)
driver.implicitly_wait(5)
driver.maximize_window()

# get discipline_cluster_list
driver.find_element(By.XPATH, "//*[contains(text(), '依學群分類查詢')]").click()
option_element_list1 = driver.find_elements(By.XPATH, "//*[contains(text(), '學群')]")
discipline_cluster_value_list = get_option_value_list(option_element_list1)

discipline_cluster_value_url = dict()

for discipline_cluster_value in discipline_cluster_value_list:
    # print(discipline_cluster_value_list)
    Select(driver.find_element(By.XPATH, "//*[contains(@id, 'LPM_sel_gsdgroup')]")).select_by_value(
        discipline_cluster_value)

    time.sleep(1)
    driver.find_element(By.XPATH, "//*[contains(@id, 'SelGsdName')]").click()
    option_element_list2 = driver.find_elements(By.XPATH,
                                                "//*[contains(@id, 'SelGsdName')]//option[contains(@value, '')]")
    # print(len(option_element_list2))
    department_value_list = get_option_value_list(option_element_list2)
    url_list = list()
    for department_value in department_value_list:
        # print(department_value_list)
        Select(driver.find_element(By.XPATH, "//*[contains(@id, 'SelGsdName')]")).select_by_value(department_value)

        driver.find_element(By.XPATH,
                            "//*[contains(@id, 'LPM_form_gsdgroup')]//*[contains(@class, 'btn') and text()='查詢']").click()

        driver.switch_to.window(driver.window_handles[1])

        # get school
        school_element_list = driver.find_elements(By.XPATH,
                                                   "//*[contains(@class, 'btn btn-outline-secondary btn-light')]")
        school_list = [school_element.text for school_element in school_element_list]
        for school in school_list:
            driver.find_element(By.XPATH,
                                "//div[contains(text(), " + "\"" + school.split('-')[
                                    1] + "\"" + ") and contains(@style, 'font-size:1.1em;text-align:left;margin:0px auto;width:70%;')]").click()

            driver.find_element(By.XPATH, "//*[contains(@class, 'LPM_colgsd_txt') and contains(text(), " + "\"" +
                                school.split('-')[1] + "\"" + ")]//parent::a").click()
            driver.switch_to.window(driver.window_handles[2])
            print(driver.current_url)
            url_list.append(driver.current_url)
            driver.close()

            driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    discipline_cluster_value_url[discipline_cluster_value] = url_list
# 抓文字
df = pd.DataFrame(discipline_cluster_value_url)
df.to_csv('111_school_url.csv', index=False)
