import pandas as pd

key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
for college_group in key_list:
    df = pd.read_csv('college_rule_18_file/' + college_group + '_college_rule.csv')
    df = df.drop_duplicates()
    print(df)
    df.to_csv('delete_duplicated_college_rule_file/' + college_group + '_college_rule.csv', index=False)
