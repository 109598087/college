from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
# key_list = ['B']
college_name_list = list()
department_name_list = list()
first_step_one_subject_list = list()
first_step_one_point_list = list()
first_step_one_ratio_list = list()
first_step_two_subject_list = list()
first_step_two_point_list = list()
first_step_two_ratio_list = list()
first_step_three_subject_list = list()
first_step_three_point_list = list()
first_step_three_ratio_list = list()
first_step_four_subject_list = list()
first_step_four_point_list = list()
first_step_four_ratio_list = list()
first_step_five_subject_list = list()
first_step_five_point_list = list()
first_step_five_ratio_list = list()

second_step_one_ratio_list = list()
second_step_two_ratio_list = list()
second_step_three_ratio_list = list()
second_step_four_ratio_list = list()
second_step_five_ratio_list = list()

second_step_all_ratio_list = list()

second_step_one_subject_list = list()
second_step_two_subject_list = list()
second_step_three_subject_list = list()
second_step_four_subject_list = list()
second_step_five_subject_list = list()

second_step_one_point_list = list()
second_step_two_point_list = list()
second_step_three_point_list = list()
second_step_four_point_list = list()
second_step_five_point_list = list()

second_step_one_all_ratio_list = list()
second_step_two_all_ratio_list = list()
second_step_three_all_ratio_list = list()
second_step_four_all_ratio_list = list()
second_step_five_all_ratio_list = list()

final_order_list = list()

thing_list = list()

order_select_list = list()


def get_information(index, df_in):
    first_step_subject = if_nothing_add_space(df_in[1].iat[index, 2])
    first_step_point = if_nothing_add_space(df_in[1].iat[index, 3])
    first_step_ratio = if_nothing_add_space(df_in[1].iat[index, 4])
    second_step_ratio = if_nothing_add_space(df_in[1].iat[index, 5])
    second_step_subject = if_nothing_add_space(df_in[1].iat[index, 7])
    second_step_point = if_nothing_add_space(df_in[1].iat[index, 8])
    second_step_all_ratio = if_nothing_add_space(df_in[1].iat[index, 9])
    return first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio


def if_nothing_add_space(word):
    # if len(word) == 0:
    #     word = ''
    return word


# driver = webdriver.Chrome('chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get('https://www.google.com/')
# driver.maximize_window()

discipline_college_url_list_dict = dict()
for discipline in key_list:
    df = pd.read_csv(discipline + 'college_id.csv')
    college_url_list = list()
    for discipline_number in df['college_id']:
        discipline_number_str = str(discipline_number)
        if len(discipline_number_str) <= 2:
            continue
        while len(discipline_number_str) < 6:
            discipline_number_str = '0' + discipline_number_str
        url = 'https://www.cac.edu.tw/apply111/system/0ColQry_for111apply_8fr51gfw/html/111_' \
              + discipline_number_str + '.htm?v=1.0'
        college_url_list.append(url)
    discipline_college_url_list_dict[discipline] = college_url_list
print(discipline_college_url_list_dict)

for discipline, college_url_list in discipline_college_url_list_dict.items():
    for url in college_url_list:
        df_url = pd.read_html(url)
        # print(df_url)
        college_name = df_url[0].iat[0, 0].split(' ')[0]
        department_name = df_url[0].iat[0, 0].split(' ')[2]
        for i in range(5):
            if i == 0:
                first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio = get_information(
                    i, df_url)
                second_step_all_ratio = df_url[1].iat[i, 6]
                final_order = df_url[1].iat[i, 10]
                # print(first_step_subject, first_step_point, first_step_ratio, second_step_ratio,
                #       second_step_subject, second_step_point, second_step_all_ratio)
                first_step_one_subject_list.append(first_step_subject)
                first_step_one_point_list.append(first_step_point)
                first_step_one_ratio_list.append(first_step_ratio)
                second_step_one_ratio_list.append(second_step_ratio)
                second_step_all_ratio_list.append(second_step_all_ratio)
                second_step_one_subject_list.append(second_step_subject)
                second_step_one_point_list.append(second_step_point)
                second_step_one_all_ratio_list.append(second_step_all_ratio)
                final_order_list.append(final_order)
            elif i == 1:
                first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio = get_information(
                    i, df_url)
                # print(first_step_subject, first_step_point, first_step_ratio, second_step_ratio,
                #       second_step_subject,
                #       second_step_point, second_step_all_ratio)
                first_step_two_subject_list.append(first_step_subject)
                first_step_two_point_list.append(first_step_point)
                first_step_two_ratio_list.append(first_step_ratio)
                second_step_two_ratio_list.append(second_step_ratio)
                second_step_two_subject_list.append(second_step_subject)
                second_step_two_point_list.append(second_step_point)
                second_step_two_all_ratio_list.append(second_step_all_ratio)
            elif i == 2:
                first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio = get_information(
                    i, df_url)
                # print(first_step_subject, first_step_point, first_step_ratio, second_step_ratio,
                #       second_step_subject,
                #       second_step_point, second_step_all_ratio)
                first_step_three_subject_list.append(first_step_subject)
                first_step_three_point_list.append(first_step_point)
                first_step_three_ratio_list.append(first_step_ratio)
                second_step_three_ratio_list.append(second_step_ratio)
                second_step_three_subject_list.append(second_step_subject)
                second_step_three_point_list.append(second_step_point)
                second_step_three_all_ratio_list.append(second_step_all_ratio)
            elif i == 3:
                first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio = get_information(
                    i, df_url)
                # print(first_step_subject, first_step_point, first_step_ratio, second_step_ratio,
                #       second_step_subject,
                #       second_step_point, second_step_all_ratio)
                first_step_four_subject_list.append(first_step_subject)
                first_step_four_point_list.append(first_step_point)
                first_step_four_ratio_list.append(first_step_ratio)
                second_step_four_ratio_list.append(second_step_ratio)
                second_step_four_subject_list.append(second_step_subject)
                second_step_four_point_list.append(second_step_point)
                second_step_four_all_ratio_list.append(second_step_all_ratio)
            elif i == 4:
                first_step_subject, first_step_point, first_step_ratio, second_step_ratio, second_step_subject, second_step_point, second_step_all_ratio = get_information(
                    i, df_url)
                # print(first_step_subject, first_step_point, first_step_ratio, second_step_ratio,
                #       second_step_subject,
                #       second_step_point, second_step_all_ratio)
                first_step_five_subject_list.append(first_step_subject)
                first_step_five_point_list.append(first_step_point)
                first_step_five_ratio_list.append(first_step_ratio)
                second_step_five_ratio_list.append(second_step_ratio)
                second_step_five_subject_list.append(second_step_subject)
                second_step_five_point_list.append(second_step_point)
                second_step_five_all_ratio_list.append(second_step_all_ratio)
        thing = df_url[2].iat[0, 4].split('※')[0]
        order_select = df_url[2].iat[6, 4]
        college_name_list.append(college_name)
        department_name_list.append(department_name)
        thing_list.append(thing)
        order_select_list.append(order_select)
        # print(thing, order_select)
        # print(first_step_one_subject_list)
        # print(first_step_one_point_list)
        # print(first_step_one_ratio_list)
        # print(first_step_two_subject_list)
        # print(first_step_two_point_list)
        # print(first_step_two_ratio_list)
        # print(first_step_three_subject_list)
        # print(first_step_three_point_list)
        # print(second_step_one_ratio_list)
        # print(second_step_all_ratio_list)
        # print(second_step_one_subject_list)
        # print(second_step_one_point_list)
        # print(second_step_one_all_ratio_list)
        # print(final_order_list)
        # print(order_select_list)

        # print(len(college_name_list))
        # print(len(department_name_list))
        # print(len(first_step_one_subject_list))
        # print(len(first_step_one_point_list))
        # print(len(first_step_one_ratio_list))
        # print(len(first_step_two_subject_list))
        # print(len(first_step_two_point_list))
        # print(len(first_step_two_ratio_list))
        # print(len(first_step_three_subject_list))
        # print(len(first_step_three_point_list))
        # print(len(first_step_three_ratio_list))
        # print(len(first_step_four_subject_list))
        # print(len(first_step_four_point_list))
        # print(len(first_step_four_ratio_list))
        # print(len(first_step_five_subject_list))
        # print(len(first_step_five_point_list))
        # print(len(first_step_five_ratio_list))
        # print(len(second_step_one_ratio_list))
        # print(len(second_step_two_ratio_list))
        # print(len(second_step_three_ratio_list))
        # print(len(second_step_two_ratio_list))
        # print(len(second_step_four_ratio_list))
        # print(len(second_step_five_ratio_list))
        # print(len(second_step_all_ratio_list))
        # print(len(second_step_one_subject_list))
        # print(len(second_step_one_point_list))
        # print(len(second_step_one_all_ratio_list))
        # print(len(second_step_two_subject_list))
        # print(len(second_step_two_point_list))
        # print(len(second_step_two_all_ratio_list))
        # print(len(second_step_three_subject_list))
        # print(len(second_step_three_point_list))
        # print(len(second_step_three_all_ratio_list))
        # print(len(second_step_four_subject_list))
        # print(len(second_step_four_point_list))
        # print(len(second_step_four_all_ratio_list))
        # print(len(second_step_five_subject_list))
        # print(len(second_step_five_point_list))
        # print(len(second_step_five_all_ratio_list))
        # print(len(final_order_list))
        # print(len(thing_list))
        # print(len(order_select_list))

    df_new = pd.DataFrame({
        'college_name': college_name_list,
        'department_name': department_name_list,
        'first_step_one_subject': first_step_one_subject_list,
        'first_step_one_point': first_step_one_point_list,
        'first_step_one_ratio': first_step_one_ratio_list,
        'first_step_two_subject': first_step_two_subject_list,
        'first_step_two_point': first_step_two_point_list,
        'first_step_two_ratio': first_step_two_ratio_list,
        'first_step_three_subject': first_step_three_subject_list,
        'first_step_three_point': first_step_three_point_list,
        'first_step_three_ratio': first_step_three_ratio_list,
        'first_step_four_subject': first_step_four_subject_list,
        'first_step_four_point': first_step_four_point_list,
        'first_step_four_ratio': first_step_four_ratio_list,
        'first_step_five_subject': first_step_five_subject_list,
        'first_step_five_point': first_step_five_point_list,
        'first_step_five_ratio': first_step_five_ratio_list,
        'second_step_one_ratio': second_step_one_ratio_list,
        'second_step_two_ratio': second_step_two_ratio_list,
        'second_step_three_ratio': second_step_three_ratio_list,
        'second_step_four_ratio': second_step_four_ratio_list,
        'second_step_five_ratio': second_step_five_ratio_list,
        'second_step_all_ratio': second_step_all_ratio_list,
        'second_step_one_subject': second_step_one_subject_list,
        'second_step_one_point': second_step_one_point_list,
        'second_step_one_all_ratio': second_step_one_all_ratio_list,
        'second_step_two_subject': second_step_two_subject_list,
        'second_step_two_point': second_step_two_point_list,
        'second_step_two_all_ratio': second_step_two_all_ratio_list,
        'second_step_three_subject': second_step_three_subject_list,
        'second_step_three_point': second_step_three_point_list,
        ' second_step_three_all_ratio': second_step_three_all_ratio_list,
        'second_step_four_subject': second_step_four_subject_list,
        'second_step_four_point': second_step_four_point_list,
        'second_step_four_all_ratio': second_step_four_all_ratio_list,
        'second_step_five_subject': second_step_five_subject_list,
        'second_step_five_point': second_step_five_point_list,
        'second_step_five_all_ratio': second_step_five_all_ratio_list,
        'final_order': final_order_list,
        'thing': thing_list,
        'order_select': order_select_list
    })

    print(df_new)
    df_new.to_csv(discipline + '_college_rule.csv', index=False)
