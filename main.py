from selenium import webdriver
import pandas as pd  # 匯入pandas套件
import time


def get_college_names():
    college_elements = driver.find_elements_by_xpath("//*[@height='28px']")
    college_texts = list()
    for college in college_elements:
        college_texts.append(college.text.split(' ')[0])
    return college_texts


def get_department_number_list(college_text):
    driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + college_text + "\"" + ')]').click()
    department_elements = driver.find_elements_by_xpath("//*[@title='校系名稱及代碼']")
    department_number_list = list()
    for department_element in department_elements:
        department_number = department_element.text.split('\n')[1].split(' ')[1]
        department_number = department_number.replace('(', '')
        department_number = department_number.replace(')', '')
        department_number_list.append(department_number)
    driver.back()
    return department_number_list


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.cac.edu.tw/apply110/system/110_aColQry4qy_forapply_o5wp6ju/TotalGsdShow.htm')
driver.implicitly_wait(3)
driver.maximize_window()
college_texts = get_college_names()

college_name_list = list()
department_name_list = list()
thing_list = list()
# for i in range(0, 20):
for i in range(21, len(college_texts)):
    department_number_list = get_department_number_list(college_texts[i])
    for department_number in department_number_list:
        df = pd.read_html(
            'https://www.cac.edu.tw/apply110/system/110_aColQry4qy_forapply_o5wp6ju/html/110_' + department_number + '.htm')
        college_name = df[0].iat[0, 0].split(' ')[0]
        department_name = df[0].iat[0, 0].split(' ')[2]
        thing = df[2].iat[0, 4].split('※')[0]
        college_name_list.append(college_name)
        department_name_list.append(department_name)
        thing_list.append(thing)
        # print(college_name, department_name, thing)

df = pd.DataFrame({
    'college_name': college_name_list,
    'department_name': department_name_list,
    'thing': thing_list
})

df.to_csv('college.csv', mode='a', header=False, index=False)
