with open('111.txt', 'r', encoding='utf-8') as file_11:
    lines = file_11.readlines()

# get 001-國立台灣大學
college_number_name_dict = dict()
for line in lines:
    if ('大學' in line or '院' in line) and '-' in line and '!' not in line and '(' not in line and '<br>' not in line:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        line = line.replace('</div>', '')
        a = line.split('-')
        college_number_name_dict[a[1]] = a[0]
# print(college_number_name_dict)

# get 臺北基督學院-基督教博雅學系
college_list = list()
for line in lines:
    if 'br' in line and ('大學' in line or '院' in line):
        line = line.replace(' ', '')
        line = line.replace('<br>', '-')
        line = line.replace('</div>', '')
        line = line.replace('\n', '')
        college_list.append(line)
        print(line)
# print(len(college_list))

final_college_department_list = list()
for college in college_list:
    college_de = college.split('-')
    final_college_department_list.append(
        college_number_name_dict[college_de[0]] + '-' + college_de[0] + '-' + college_de[1])
print(final_college_department_list)
print(len(final_college_department_list))

import pandas as pd  # 匯入pandas套件
from urllib import parse

df_list = list()
url = 'https://www.cac.edu.tw/cacportal/jbcrc/LearningPortfolios_MultiQuery_ppa/LPM_readfile_html.php?fileid='
for final_college_department in final_college_department_list:
    # print(parse.quote(final_college_department))
    # print(type(parse.quote(final_college_department)))
    try:
        url = 'https://www.cac.edu.tw/cacportal/jbcrc/LearningPortfolios_MultiQuery_ppa/LPM_readfile_html.php?fileid=' + parse.quote(
            final_college_department)
        df = pd.read_html(url, encoding='utf-8')
        # print(df)
        df_list.append(df)
    except:
        print(final_college_department)
        df_list.append('呵呵')
df_111 = pd.DataFrame({
    'college': final_college_department_list,
    'df': df_list
})
print(len(df_list))
df_111.to_csv('college111.csv')
