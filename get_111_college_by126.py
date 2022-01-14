import time

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://www.google.com/')
driver.maximize_window()
df = pd.read_csv('discipline_cluster_department.csv')
college_category = ''
college_group1 = ''
college_group2 = ''
key_dict = {'資訊學群': 'A', '工程學群': 'B', '數理化學群': 'C', '醫藥衛生學群': 'D', '生命科學學群': 'E', '生物資源學群': 'F', '地球環境學群': 'G',
                    '建築設計學群': 'H', '藝術學群': 'I', '社會心理學群': 'J', '大眾傳播學群': 'K', '外語學群': 'L', '文史哲學群': 'M', '教育學群': 'N',
                    '法政學群': 'O', '管理學群': 'P', '財經學群': 'Q', '遊憩運動學群': 'R'}
nan_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 18, 19, 20, 21, 22, 27, 28, 29, 44, 45, 46, 49, 50, 56, 64,
            65, 66, 67, 71, 77, 78, 80, 81, 90, 95, 96, 105, 108, 109, 112, 117, 118, 119, 120, 121, 130]
# 找collego各學類
for i in range(len(df['id'])):
    print(i, df.iat[i, 0], df.iat[i, 1], df.iat[i, 2])
    url_discipline = 'https://collego.edu.tw/Highschool/MajorIntro?current_major_id=' + str(df.iat[i, 0])
    print(url_discipline)
    is_college_group2 = 0
    college_category = df.iat[i, 1]
    college_group1 = df.iat[i, 2]
    college_group1_csv_name = 'add_found_column_to_college_rule_file/' + key_dict[college_group1] + '_college_rule.csv'
    college_group1_df = pd.read_csv(college_group1_csv_name)
    if i in nan_list:
        is_college_group2 = 1
        college_group2 = df.iat[i, 3]
        print(college_group2)
        college_group2_csv_name = 'add_found_column_to_college_rule_file/' + key_dict[college_group2] + '_college_rule.csv'
        college_group2_df = pd.read_csv(college_group2_csv_name)

    driver.get(url_discipline)
    driver.find_element(By.XPATH, "//*[contains(@data, 'tab4default')]").click()
    # 該學類底下的所有校系element
    department_element_list = driver.find_elements(By.XPATH, "//*[contains(@id, 'table')]//tr")
    row_index_list = list()
    discipline_list = list()
    department_list = list()
    discipline_value1 = ''
    discipline_value2 = ''
    # 一個一個抓網頁上的校系
    for department in department_element_list:
        department_value = department.text.split()
        # 校名
        school_name_value = department_value[0]
        # 系名
        department_name_value = department_value[1]
        if school_name_value == '學校' and department_name_value == '系組名稱':
            continue
        print('29', school_name_value, department_name_value)

        # 找到第一個學群csv
        if college_group1 is not '':
            row_index = college_group1_df.index[(college_group1_df['college_name'] == school_name_value) & (
                    college_group1_df['department_name'] == department_name_value)].to_list()
            if len(row_index) > 0:
                row_index_list.append(row_index[0])
                discipline_list.append(school_name_value)
                department_list.append(department_name_value)
                column_index = college_group1_df.columns.get_loc("found")
                college_group1_df.iloc[row_index, column_index] = 1

        if is_college_group2:
            row_index = college_group2_df.index[(college_group2_df['college_name'] == school_name_value) & (
                    college_group2_df['department_name'] == department_name_value)].to_list()
            if len(row_index) > 0:
                column_index = college_group2_df.columns.get_loc("found")
                college_group2_df.iloc[row_index, column_index] = 1
    # 每個學類college_category一個csv
    print('hi')
    print(college_group1_df)
    # college_group1_df.to_csv('add_found_column_to_college_rule_file/' + key_dict[college_group1] + '_college_rule.csv', index=False)
    # if is_college_group2:
    #     college_group2_df.to_csv(
    #         'add_found_column_to_college_rule_file/' + key_dict[college_group2] + '_college_rule.csv', index=False)
    college_group1_df.iloc[row_index_list].to_csv('college_rule_126_file/' + college_category + '_college_rule_126.csv', index=False)

# for i in range(1, 133):
#     not_in_list = [8, 124, 127, 128, 129, 130, 131]
#     print(i)
#     if i in not_in_list:
#         continue
#     else:
#         url_discipline = 'https://collego.edu.tw/Highschool/MajorIntro?current_major_id=' + str(i)
#
#     driver.get(url_discipline)
#     driver.find_element(By.XPATH, "//*[contains(@data, 'tab4default')]").click()
#     # 該學類底下的所有校系element
#     department_element_list = driver.find_elements(By.XPATH, "//*[contains(@id, 'table')]//tr")
#     row_index_list = list()
#     discipline_list = list()
#     department_list = list()
#     discipline_value1 = ''
#     discipline_value2 = ''
#     # 一個一個抓網頁上的校系
#     for department in department_element_list:
#         department_value = department.text.split()
#         # 校名
#         department_value1 = department_value[0]
#         # 系名
#         department_value2 = department_value[1]
#         if department_value1 == '學校' and department_value2 == '系組名稱':
#             continue
#         print('29', department_value1, department_value2)
#
#         # 找到對應的1 or 2學群
#         key_dict = {'資訊學群': 'A', '工程學群': 'B', '數理化學群': 'C', '醫藥衛生學群': 'D', '生命科學學群': 'E', '生物資源學群': 'F', '地球環境學群': 'G',
#                     '建築設計學群': 'H', '藝術學群': 'I', '社會心理學群': 'J', '大眾傳播學群': 'K', '外語學群': 'L', '文史哲學群': 'M', '教育學群': 'N',
#                     '法政學群': 'O', '管理學群': 'P', '財經學群': 'Q', '遊憩運動學群': 'R'}
#         for j in range(0, 127):
#             print('36', df.iat[j, 1])
#             print('37', df.iat[j, 2])
#             print('38', df.iat[j, 3])
#             if df.iat[j, 2] in key_dict.keys():
#                 discipline_value1 = key_dict[df.iat[j, 2]]
#
#             if df.iat[j, 3] in key_dict.keys():
#                 discipline_value2 = key_dict[df.iat[j, 3]]
#
#             if discipline_value1 is not '' and discipline_value2 is not '':
#                 break
#         found = 0
#         # 找到第一個學群csv
#         if discipline_value1 is not '':
#             df_discipline1 = pd.read_csv(discipline_value1 + '_college_rule.csv')
#             row_index = df_discipline1.index[(df_discipline1['college_name'] == department_value1) & (
#                         df_discipline1['department_name'] == department_value2)].to_list()
#             if len(row_index) > 0:
#                 row_index_list.append(row_index[0])
#                 discipline_list.append(department_value1)
#                 department_list.append(department_value2)
#
#     df_discipline1 = pd.read_csv(discipline_value1 + '_college_rule.csv')
#
#     df_discipline1.iloc[row_index_list].to_csv(str(i) + '_college_rule_126.csv', index=False)
#
#     # 加上 found
#     df_discipline1['found'] = [0 for i in range(len(df_discipline1['college_name']))]
#     for a in range(len(department_list)):
#         row_index = df_discipline1.index[(df_discipline1['college_name'] == discipline_list[a])
#                                          & (df_discipline1['department_name'] == department_list[a])]
#         column_index = df_discipline1.columns.get_loc("found")
#         df_discipline1.iloc[row_index, column_index] = 1
#     print('hihi')
#     print(df_discipline1)
#     df_discipline1.to_csv(str(i) + 'new_df_college_rule_126.csv', index=False)
