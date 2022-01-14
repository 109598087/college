import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://www.google.com/')
driver.maximize_window()
df = pd.read_csv('discipline_cluster_department.csv')
# 找collego各學類
for i in range(1, 133):
    not_in_list = [8, 124, 127, 128, 129, 130, 131]
    print(i)
    if i in not_in_list:
        continue
    else:
        url_discipline = 'https://collego.edu.tw/Highschool/MajorIntro?current_major_id=' + str(i)

    driver.get(url_discipline)
    driver.find_element(By.XPATH, "//*[contains(@data, 'tab4default')]").click()
    department_element_list = driver.find_elements(By.XPATH, "//*[contains(@id, 'table')]//tr")
    # 學類裡的各校系
    row_index_list = list()
    discipline_list = list()
    department_list = list()
    discipline_value1 = ''
    discipline_value2 = ''
    # 一個一個抓網頁上的校系
    for department in department_element_list:
        department_value = department.text.split()
        # 校系名
        department_value1 = department_value[0]
        department_value2 = department_value[1]
        if department_value1 == '學校' and department_value2 == '系組名稱':
            continue
        print('29', department_value1, department_value2)

        # 找到對應的1 or 2學群
        key_dict = {'資訊學群': 'A', '工程學群': 'B', '數理化學群': 'C', '醫藥衛生學群': 'D', '生命科學學群': 'E', '生物資源學群': 'F', '地球環境學群': 'G',
                    '建築設計學群': 'H', '藝術學群': 'I', '社會心理學群': 'J', '大眾傳播學群': 'K', '外語學群': 'L', '文史哲學群': 'M', '教育學群': 'N',
                    '法政學群': 'O', '管理學群': 'P', '財經學群': 'Q', '遊憩運動學群': 'R'}
        for j in range(0, 127):
            print('36', df.iat[j, 1])
            if df.iat[j, 2] in key_dict.keys():
                discipline_value1 = key_dict[df.iat[j, 2]]

            if df.iat[j, 3] in key_dict.keys():
                discipline_value2 = key_dict[df.iat[j, 3]]

            if discipline_value1 is not '' and discipline_value2 is not '':
                break
        found = 0
        # 找到第一個學群csv
        if discipline_value1 is not '':
            df_discipline1 = pd.read_csv(discipline_value1 + '_college_rule.csv')
            row_index = df_discipline1.index[(df_discipline1['college_name'] == department_value1) & (
                        df_discipline1['department_name'] == department_value2)].to_list()
            if len(row_index) > 0:
                row_index_list.append(row_index[0])
                discipline_list.append(department_value1)
                department_list.append(department_value2)

    df_discipline1 = pd.read_csv(discipline_value1 + '_college_rule.csv')

    df_discipline1.iloc[row_index_list].to_csv(str(i) + '_college_rule_126.csv', index=False)

    # 加上 found
    df_discipline1['found'] = [0 for i in range(len(df_discipline1['college_name']))]
    for a in range(len(department_list)):
        row_index = df_discipline1.index[(df_discipline1['college_name'] == discipline_list[a])
                                         & (df_discipline1['department_name'] == department_list[a])]
        column_index = df_discipline1.columns.get_loc("found")
        df_discipline1.iloc[row_index, column_index] = 1
    print('hihi')
    print(df_discipline1)
    df_discipline1.to_csv(str(i) + 'new_df_college_rule_126.csv', index=False)
