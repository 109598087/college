import pandas as pd
import csv

key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
# key_list = ['A']
# for 18 college group
for college_group in key_list:
    df = pd.read_csv('add_found_column_to_college_rule_file/' + college_group + '_college_rule.csv')
    print(df)

    important_subject_dict = {}
    # 目標:important_all_report_dict = {'修課紀錄': {'A': 245}, '課程學習成果': {'B': 245, 'C': 9}}
    important_all_report_dict = {}
    print(college_group, important_subject_dict)
    # for all 校系
    for i in range(len(df['college_name'])):
        # for subject_dict
        for j in range(5):
            if df.iat[i, 2 + 3 * j] not in important_subject_dict.keys():
                important_subject_dict[df.iat[i, 2 + 3 * j]] = 1
            else:
                important_subject_dict[df.iat[i, 2 + 3 * j]] += 1

        # for 學習歷程
        # df.iat[i, 39] = 項目：修課紀錄(A)、課程學習成果(B、C、D)、多元表現(F、J、M、N)、學習歷程自述(P、Q)、其他(R.本系個人資料表、S.自傳(學生自述)、T.其他有利審查之證明)
        all_report_item = df.iat[i, 39].split(')')
        # all_report_item = ['項目：修課紀錄(A', '、課程學習成果(B、C、D', '、多元表現(F、J、M、N', '、學習歷程自述(P、Q', '、其他(R.本系個人資料表、S.自傳(學生自述', '、T.其他有利審查之證明', ' ']
        for k in range(len(all_report_item) - 1):
            report_name = ''
            report_item_id_list = []
            important_report_dict = {}  # 目標:important_report_dict = {'B': 245, 'C': 9}
            # 區分['、課程學習成果(B、C、D', '、其他(R.本系個人資料表、S.自傳(學生自述', '、T.其他有利審查之證明']
            if '(' in all_report_item[k] and '其他' not in all_report_item[k]:
                report = all_report_item[k].split('(')
                # 區分['項目：修課紀錄(A', '、課程學習成果(B、C、D']
                if '、' in report[0]:
                    report_name = report[0][1:]
                elif '：' in report[0]:
                    report_name = report[0][3:]
                # print('report_name=', report_name)
                # 區分'A' or 'B、C、D'
                if '、' in report[1]:
                    report_item_id_list = report[1].split('、')
                else:
                    report_item_id_list = [report[1]]
            else:
                report_name = '其他'
                if 'R' in all_report_item[k]:
                    report_item_id_list.append('R')
                if 'S' in all_report_item[k]:
                    report_item_id_list.append('S')
                if 'T' in all_report_item[k]:
                    report_item_id_list.append('T')
            # print('report_item_id_list=', report_item_id_list)

            # 組成important_report_dict
            for m in range(len(report_item_id_list)):
                if report_item_id_list[m] not in important_report_dict.keys():
                    important_report_dict[report_item_id_list[m]] = 1
                else:
                    important_report_dict[report_item_id_list[m]] += 1
            # print('important_report_dict=', important_report_dict)

            # 組成important_all_report_dict
            if report_name not in important_all_report_dict.keys():
                important_all_report_dict[report_name] = important_report_dict
            else:
                for report_id in important_report_dict.keys():
                    if report_id not in important_all_report_dict[report_name].keys():
                        important_all_report_dict[report_name][report_id] = important_report_dict[report_id]
                    else:
                        important_all_report_dict[report_name][report_id] += 1

    print('important_all_report_dict', college_group,  important_all_report_dict)
    print('important_subject_dict', college_group, important_subject_dict)
    # {'修課紀錄': {'A': 114}, '課程學習成果': {'B': 99, 'E': 38, 'C': 39, 'D': 7}}
    # to {'A': 114, 'B': 99, 'E': 38, 'C': 39, 'D': 7}
    important_all_report_without_report_name_dict = {}
    for report_key in important_all_report_dict:
        important_all_report_without_report_name_dict.update(important_all_report_dict[report_key])
    important_all_report_without_report_name_dict = dict(sorted(important_all_report_without_report_name_dict.items(),
                                                                key=lambda item: item[1], reverse=True))
    # write dict to csv
    with open('care_report_18/' + college_group + '_care_report_without_report_name.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['report_id', 'count'])
        for k, v in important_all_report_without_report_name_dict.items():
            writer.writerow([k, v])

    important_subject_dict = dict(sorted(important_subject_dict.items(), key=lambda item: item[1], reverse=True))
    with open('care_subject_18/' + college_group + '_care_subject.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['subject_id', 'count'])
        for k, v in important_subject_dict.items():
            writer.writerow([k, v])
