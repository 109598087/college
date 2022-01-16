import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
key_list = ['I']

for college_group in key_list:
    df = pd.read_csv('care_report_18/' + college_group + '_care_report_without_report_name.csv')
    print(df)
    report_id_list = []
    report_count_list = []
    else_report_id_str = 'others('
    else_report_count_sum = 0
    for i in range(len(df['report_id'])):
        if i < 9:
            report_id_list.append(df.iat[i, 0])
            report_count_list.append(df.iat[i, 1])
        elif 9 <= i < len(df['report_id']) - 1:
            else_report_id_str += df.iat[i, 0] + ','
            else_report_count_sum += df.iat[i, 1]
        else:
            else_report_id_str += df.iat[i, 0] + ')'
            else_report_count_sum += df.iat[i, 1]
    report_id_list.append(else_report_id_str)
    report_count_list.append(else_report_count_sum)
    print(report_id_list)
    print(report_count_list)
    plt.pie(report_count_list, labels=report_id_list, autopct='%1.1f%%')
    # plt.legend(patches, df['report_id'], loc="best")
    plt.axis('equal')
    plt.savefig('care_report_18/' + college_group + 'top_nine.png', bbox_inches='tight')
    plt.show()
    # fig = px.pie(df, values='count', names='report_id', title='Report')
    # fig.show()

