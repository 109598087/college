import pandas as pd

key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
for discipline in key_list:
    df = pd.read_csv('college_rule_18_file/' + discipline + '_college_rule.csv')
    print(df)
    df['found'] = [0 for i in range(len(df['college_name']))]
    df.to_csv('add_found_column_to_college_rule_file/' + discipline + '_college_rule.csv', index=False)
