import re
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def get_option_value_list(option_element_list):
    value_list = list()
    # key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    for option_element in option_element_list:
        # print(option_element.get_attribute('value'))
        if option_element.get_attribute('value') is not None:
            value_list.append(option_element.get_attribute('value'))
        # if option_element.get_attribute('value') in key_list:
        #     value_list.append(option_element.get_attribute('value'))
    return value_list


driver = webdriver.Chrome('chromedriver.exe')
url_111 = 'https://www.cac.edu.tw/apply111/system/0ColQry_for111apply_8fr51gfw/findgsdgroup.htm'
driver.get(url_111)
driver.implicitly_wait(5)
driver.maximize_window()

option_element_list = driver.find_elements(By.XPATH, "//*[contains(text(), '學群')]")
print(option_element_list)
discipline_cluster_value_list = get_option_value_list(option_element_list)
print(discipline_cluster_value_list)

discipline_cluster_value_url = dict()

all_college_id_list = list()

for discipline_cluster_value in discipline_cluster_value_list:
    # print(discipline_cluster_value_list)
    Select(driver.find_element(By.XPATH, "//*[contains(@name, 'gcode')]")).select_by_value(
        discipline_cluster_value)
    driver.find_element(By.XPATH, "//*[contains(@name, 'query')]").click()

    time.sleep(1)
    driver.find_element(By.XPATH, "//*[contains(@name, 'GsdName')]").click()
    option_element_list2 = driver.find_elements(By.XPATH,
                                                "//*[contains(@name, 'GsdName')]//option[contains(@value, '')]")
    # print(len(option_element_list2))
    department_value_list = get_option_value_list(option_element_list2)
    # print(department_value_list)
    url_list = list()
    for department_value in department_value_list:
        # print(department_value_list)
        Select(driver.find_element(By.XPATH, "//*[contains(@name, 'GsdName')]")).select_by_value(department_value)

        driver.find_element(By.XPATH, "//*[contains(@name, 'query')]").click()

        college_id_element_list = driver.find_elements(By.XPATH, "//*[contains(text(), '(') and contains(text(), ')')]")
        for college_id_element in college_id_element_list:
            all_college_id_list.append(college_id_element.text.replace('(', '').replace(')', ''))
            print(college_id_element.text.replace('(', '').replace(')', ''))
        driver.find_element(By.XPATH, "//input[@value='回上一頁']").click()
    driver.get('https://www.cac.edu.tw/apply111/system/0ColQry_for111apply_8fr51gfw/findgsdgroup.htm')
print(all_college_id_list)
for college_id in all_college_id_list:
    if len(re.findall(r'-?\d+\.?\d*', college_id)) != 0:
        all_college_id_list += re.findall(r'-?\d+\.?\d*', college_id)
pd.DataFrame({
    'college_id': all_college_id_list,
}).to_csv('college_id.csv', index=False)

# driver.find_element(By.XPATH,
#                     "//*[contains(@id, 'LPM_form_gsdgroup')]//*[contains(@class, 'btn') and text()='查詢']").click()
#
#     # 獲取開啟的多個視窗控制
#     driver.switch_to.window(driver.window_handles[1])
#
#     # get school
#     school_element_list = driver.find_elements(By.XPATH,
#                                                "//*[contains(@class, 'btn btn-outline-secondary btn-light')]")
#     school_list = [school_element.text for school_element in school_element_list]
#     for school in school_list:
#         driver.find_element(By.XPATH,
#                             "//div[contains(text(), " + "\"" + school.split('-')[
#                                 1] + "\"" + ") and contains(@style, 'font-size:1.1em;text-align:left;margin:0px auto;width:70%;')]").click()
#         time.sleep(1)
#         driver.find_element(By.XPATH, "//*[contains(@class, 'LPM_colgsd_txt') and contains(text(), " + "\"" +
#                             school.split('-')[1] + "\"" + ")]//parent::a").click()
#         driver.switch_to.window(driver.window_handles[2])
#         print(driver.current_url)
#         url_list.append(driver.current_url)
#         driver.close()
#
#         driver.switch_to.window(driver.window_handles[1])
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])
# # discipline_cluster_value_url[discipline_cluster_value] = url_list
#
# df = pd.DataFrame({
#     discipline_cluster_value: url_list
# })
# df.to_csv(discipline_cluster_value + '111_school_url.csv', index=False)
