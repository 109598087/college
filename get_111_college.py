import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

for i in range(18):
    value_xd = str(i)
    df = pd.read_csv(value_xd + '111_school_url.csv')

    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://www.google.com/')
    driver.maximize_window()

    school_list = list()
    a_class_list = list()

    chinese_list = list()
    math_list = list()
    science_list = list()
    social_list = list()
    art_list = list()
    tech_list = list()
    all_list = list()
    health_list = list()
    total_list = list()

    paper_report_list = list()
    doing_work_list = list()
    science_work_list = list()
    social_work_list = list()

    a = list()
    b = list()
    c = list()
    d = list()
    e = list()
    f = list()
    g = list()
    h = list()

    x = list()
    y = list()
    z = list()

    for url in df[value_xd]:
        driver.get(url)
        school_a_class = driver.find_element(By.XPATH, "//span").text
        school_list.append(school_a_class.split('-')[0])
        a_class_list.append(school_a_class.split('-')[1])

        class_record = driver.find_element(By.XPATH,
                                           "//td[contains(text(), '修課') and contains(@style, 'center')]/following-sibling::*[contains(@style, '910px')]").text

        chinese_list.append(True if '語文' in class_record else False)
        math_list.append(True if '數學' in class_record else False)
        science_list.append(True if '自然' in class_record else False)
        social_list.append(True if '社會' in class_record else False)
        art_list.append(True if '藝術' in class_record else False)
        tech_list.append(True if '科技' in class_record else False)
        all_list.append(True if '綜合' in class_record else False)
        health_list.append(True if '健康' in class_record else False)
        total_list.append(True if '總成績' in class_record else False)

        class_result = driver.find_element(By.XPATH,
                                           "//td[contains(text(), '課程') and contains(@style, 'center')]/following-sibling::*").text

        paper_report_list.append(True if '書面報告' in class_result else False)
        doing_work_list.append(True if '實作作品' in class_result else False)
        science_work_list.append(True if '自然' in class_result else False)
        social_work_list.append(True if '社會' in class_result else False)

        multi_result = driver.find_element(By.XPATH,
                                           "//td[contains(text(), '多元') and contains(@style, 'center')]/following-sibling::*").text

        a.append(True if '高中自主學習計畫與成果' in class_result else False)
        b.append(True if '社團活動經驗' in class_result else False)
        c.append(True if '擔任幹部經驗' in class_result else False)
        d.append(True if '服務學習經驗' in class_result else False)
        e.append(True if '競賽表現' in class_result else False)
        f.append(True if '非修課紀錄成果作品' in class_result else False)
        g.append(True if '檢定證照' in class_result else False)
        h.append(True if '特殊優良表現證明' in class_result else False)

        stu_his_result = driver.find_element(By.XPATH,
                                             "//td[contains(text(), '學習歷程') and contains(@style, 'center')]/following-sibling::*").text

        x.append(True if '高中學習歷程反思' in class_result else False)
        y.append(True if '就讀動機' in class_result else False)
        z.append(True if '未來學習計畫與生涯規劃' in class_result else False)

    df = pd.DataFrame({
        '學校': school_list,
        '系組': a_class_list,
        'chinese_list': chinese_list,
        'math_list': math_list,
        'science_list': science_list,
        'social_list': social_list,
        'art_list': art_list,
        'tech_list': tech_list,
        'all_list': all_list,
        'health_list': health_list,
        'total_list': total_list,
        'paper_report_list': paper_report_list,
        'doing_work_list': doing_work_list,
        'science_work_list': science_work_list,
        'social_work_list': social_work_list,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'x': x,
        'y': y,
        'z': z,
    })

    df.to_csv(value_xd + 'result.csv')
